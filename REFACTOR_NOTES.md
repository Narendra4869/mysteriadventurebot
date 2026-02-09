# FIRMAMEN Game — Refactor #2: Trajectory-Based Ending Logic

## 🎯 Problem Statement (dari User)

Tiga masalah desain terdeteksi dalam sistem sebelumnya yang masih "stat-based":

### ❗ Masalah 1: TRUE ENDING masih terlalu "lucky loss"
**Sebelumnya:**
```python
if knowledge >= 6 and hesitation_level >= 7 and coalition < 5:
    # TRUE ENDING
```

**Masalah:** Pemain bisa mengabaikan stat kehilangan coalition secara random, padahal ending ini seharusnya tentang **penundaan moral**, bukan keberuntungan negatif stat.

### ❗ Masalah 2: Hesitation tidak "truly lock" pilihan
**Sebelumnya:** hesitation tinggi hanya membuat narasi memburuk, tapi semua pilihan masih tersedia.

**Masalah:** Setelah hesitation >= 8, pemain seharusnya TIDAK bisa memilih "koordinasi kolektif"—pilihan itu sdh hilang secara permanen, bukan hanya "kurang efektif".

### ❗ Masalah 3: GOOD ENDING masih bisa dioptimasi
**Sebelumnya:** Pemain bisa late-correct di Scene 4 (mengumpulkan stat yang cukup), masih terasa seperti "gameplay optimization".

**Masalah:** GOOD ENDING harus membutuhkan **early commitment**, bukan late stat fix. Jika pemain hesitate terlalu banyak di awal, GOOD ENDING harus menjadi impossible selamanya.

---

## ✅ Solusi Implementasi

### 1️⃣ Trajectory Tracking Variables

Mengganti `delayed_action` (binary) + `moral_signal_count/ignored` (complex) dengan **satu metric yang jelas**:

```python
first_hesitation_scene = None      # Kapan pemain pertama kali hesitate?
hesitation_action_count = 0        # Berapa kali pemain pilih untuk hesitate/menunggu?
```

**Logic:**
- `first_hesitation_scene`: Track apakah pemain hesitate **sejak awal** (Scene 1-2) atau late
- `hesitation_action_count`: Count **berapa kali** pemain memilih pilihan hesitate di semua scenes
  - Scene 1, Choice 2: +1
  - Scene 2, Choice 3: +1
  - Scene 3, Choice 3: +1
  - Scene 4, Choice 3: +1

### 2️⃣ Refactor TRUE ENDING — Trajectory-Based

**Kondisi Baru:**
```python
if (knowledge >= 6 and hesitation_level >= 7 and 
    first_hesitation_scene is not None and first_hesitation_scene <= 2 and
    hesitation_action_count >= 2):
    # TRUE ENDING: "KEBENARAN YANG TERLAMBAT"
```

**Arti:**
- `knowledge >= 6`: Pemain tahu segalanya
- `hesitation_level >= 7`: Pemain REPEATEDLY membuat pilihan hesitate
- `first_hesitation_scene <= 2`: Hesitasi DIMULAI sejak awal (Scene 1 atau 2), bukan late
- `hesitation_action_count >= 2`: Minimal DUA kali pilih hesitate → **pattern yang konsisten**

**Filosofi:**
"Aku melihat masalah sejak awal. Aku layak bertindak. Tapi aku terus menunggu."

#### Bedanya dengan BAD ENDING:
- TRUE ENDING: Knowledge tinggi + Hesitation trajectory jelas = Dunia discover truth tapi terlambat
- BAD ENDING: Knowledge rendah ATAU no hesitation trajectory = Ilusi terus bertahan

### 3️⃣ Refactor GOOD ENDING — Early Commitment Required

**Kondisi Baru:**
```python
elif (knowledge >= 5 and urgency >= 5 and coalition >= 5 and 
      hesitation_action_count <= 1):
    # GOOD ENDING: "LANGIT YANG REWEL"
```

**Arti:**
- `hesitation_action_count <= 1`: Pemain BOLEH hesitate maksimal 1x saja
- Jika `hesitation_action_count >= 2`, GOOD ENDING IMPOSSIBLE selamanya (menjadi BAD ENDING)

**Filosofi:**
"Aku berkomitmen sejak awal. Saya tidak terlalu menunggu-nunggu. Kami berubah bersama."

#### Bedanya dari sebelumnya:
- **Sebelumnya:** `hesitation_level <= 5` (masih bisa late fix dengan aggressive action)
- **Sekarang:** `hesitation_action_count <= 1` (irrevocable—early hesitation memblokir GOOD ENDING)

### 4️⃣ Scene-Level Narrative Locking

**Scene 4 — If hesitation >= 8:**
```
"*** JENDELA WAKTU SUDAH TERTUTUP ***"
Pilihan hanya:
1. Bertindak sendiri
2. Tidak melakukan apa-apa

[Pilihan "Koordinasi kolektif" sudah HILANG]
```

**Narrative justification:**
"Aliansi Anda telah bercerai. Tidak ada yang mendengarkan Anda."

---

## 📊 Ending Mapping (Trajectory-Based)

| Ending | Condition | Player Pattern | Narrative Result |
|--------|-----------|-----------------|-----------------|
| **TRUE** | knowledge ≥6 + hesitation ≥7 + first_hesitation ≤2 + actions ≥2 | Hesitate dari awal, repeatedly | Dunia tahu kebenaran, tapi terlambat; ribuan sudah mati |
| **GOOD** | knowledge ≥5 + urgency ≥5 + coalition ≥5 + actions ≤1 | Early commitment, minimal wait | Perubahan perlahan, ada resistance, tapi komunitas tetap |
| **BAD** | Semua kondisi lain | Inconsistent/late/passive | Gereja bertahan; ilusi berlanjut |

---

## 🎮 Player Experience Changes

### Sebelumnya:
- Pemain bisa "optimize" TRUE ENDING dengan formula stat
- GOOD ENDING terasa seperti "reach the right numbers"
- Hesitation hanya narasi, tidak mechanical lock

### Sekarang:
- TRUE ENDING fokus pada **when & how consistently** hesitate, bukan stat akhir
- GOOD ENDING membutuhkan **early decision**, tidak bisa diperbaiki late
- Hesitation >= 8 **benar-benar menghilangkan pilihan**, bukan sekadar memperburuk outcome

### Efek:
- ✅ Tidak ada "optimal play" yang dingin—setiap trajectory terasa *earned*
- ✅ Waktu = mekanik, bukan flavor text
- ✅ Setiap ending mencerminkan **pola keputusan**, bukan angka beruntung

---

## 🔧 Technical Details

### Variables Tracking
```python
# Per game instance
hesitation_level = 0           # Cumulative (0-10+)
first_hesitation_scene = None  # 1, 2, or None
hesitation_action_count = 0    # How many times player chose to wait
```

### Scene 4 Architecture (Narrative Lock)
```
if hesitation_level >= 8:
    Show "JENDELA WAKTU SUDAH TERTUTUP"
    Only available: Choice 1 (solo action) or Choice 2 (nothing)
    # Choice 2 would be "Koordinasi" — REMOVED
    
elif hesitation_level >= 6:
    Show warning
    All choices available (but warning flags consequences)
    
else:
    Normal flow, all 3 choices available
```

### Ending Determination (check_ending)
```python
# Check TRUE ENDING first (most specific)
if knowledge >= 6 AND hesitation >= 7 AND first_hesitation <= 2 AND actions >= 2:
    TRUE ENDING
elif knowledge >= 5 AND urgency >= 5 AND coalition >= 5 AND actions <= 1:
    GOOD ENDING
else:
    BAD ENDING
```

---

## 📝 Key Philosophical Insight

**"Delay is not neutral—it is a choice with consequences."**

- Tidak ada "waiting for perfect information" tanpa cost
- Setiap scene yang pass tanpa action = commit ke trajectory tertentu
- TRUE ENDING bukan "reward for knowing everything", tapi "consequence of knowing too late"
- GOOD ENDING bukan "easy path", tapi "early courage"

---

**Last Updated:** 2026-02-09  
**Status:** Full trajectory-based refactor complete
