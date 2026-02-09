# FIRMAMEN: Design Philosophy & Technical Implementation

## 🎭 Narrative Philosophy

**Core Thesis**: "Pengetahuan tanpa ketepatan waktu adalah bentuk kebohongan lain."

Game ini bukan tentang optimasi stat atau "game over conditions". Ini adalah cerita tentang:
- Temporal ethics: kapan Anda bertindak lebih penting daripada apa yang Anda ketahui
- Institutional decay: sistem otoriter runtuh oleh timing, bukan oleh kebenaran semata
- Collective action: keadilan membutuhkan solidaritas, bukan hanya pemahaman
- Moral responsibility: menunggu dengan data sempurna = kelalaian moral yang diam-diam

---

## 🔧 Technical System: `hesitation_level`

### Konsep
Mengganti boolean `delayed_action` dengan gradual accumulator `hesitation_level` (0-10+):

```python
hesitation_level = 0  # Tracks accumulated moral hesitation
```

### Mechanics

**Setiap pilihan "menunggu" menambahkan poin:**
- Scene 1, Choice 2: +1 (pemain diam)
- Scene 2, Choice 3: +2 (pemain menunda observasi)
- Scene 3, Choice 3: +3 (pemain mengejar data sempurna)
- Scene 4, Choice 3: +3 (pilihan menunggu terakhir)

**Threshold Consequences:**
```
hesitation_level 0-3:  Pemain belum terikat; keputusan masih reversible
hesitation_level 4-6:  NPC mulai jauh; allies kehilangan kepercayaan
hesitation_level 7+:   Jendela aksi kolektif tertutup; sadur pada saksi pasif
hesitation_level 10+:  Sistem runtuh di luar kontrol pemain
```

### Narrative Feedback (Skala Otomatis)

Setiap scene menampilkan feedback yang berbeda berdasarkan akumulasi:

**Scene 2:**
- `hesitation_level < 4`: Profesor mudah dihubungi
- `hesitation_level >= 4`: Profesor hilang; data info tentang Gereja mengetahui

**Scene 3:**
- `hesitation_level < 5`: "Mereka menunggu keputusan Anda"
- `hesitation_level 5-6`: "Tiga orang baru dieksekusi... Aliansi menunggu"
- `hesitation_level >= 7`: "Aliansi Anda mulai runtuh... waktu sudah berakhir"

**Scene 4:**
- `hesitation_level < 6`: "Anda masih memiliki aliansi"
- `hesitation_level 6-8`: "**PERINGATAN**: Waktu untuk aksi kolektif hampir usai"
- `hesitation_level >= 8`: "**TITIK TIDAK BISA KEMBALI TELAH TERLAMPAUI**"

---

## 📊 Ending Logic (Tidak Berdasarkan Optimization)

### Ending 1: KEBENARAN YANG TERLAMBAT (TRUE ENDING)
```
TRIGGERED BY:
  knowledge >= 6 
  AND hesitation_level >= 7 
  AND coalition < 5

RESULT:
- Dunia discovers truth (sistem runtuh otomatis)
- Ribuan sudah mati sebelum pengetahuan terungkap
- Protagonist adalah saksi dengan semua jawaban, tapi tidak ada yang mendengarkan
- Kemenangan intelektual, kekalahan moral

THEME:
"Pengetahuan tanpa ketepatan waktu adalah bentuk kebohongan lain."
```

### Ending 2: LANGIT YANG REWEL (GOOD ENDING)
```
TRIGGERED BY:
  knowledge >= 5 
  AND urgency >= 5 
  AND coalition >= 5 
  AND hesitation_level <= 5

RESULT:
- Langit palsu tidak langsung runtuh, tapi terdisintegrasi perlahan
- Gereja melawan, tapi koalisi pemain bertahan
- Ada bekas luka: kepercayaan hancur, trauma sosial, instabilitas
- Bukan kemenangan bersih, tapi pilihan bersama

THEME:
"Kemenangan yang berdebu lebih bermakna daripada keputusan sempurna yang terpurbait."
```

### Ending 3: GEREJA BERTAHAN (BAD ENDING)
```
TRIGGERED BY:
- Semua skenario lain yang tidak memenuhi TRUE or GOOD criteria

RESULT:
- Sistema bertahan; ilusi terus berlanjut
- Jika knowledge tinggi: pemain tahu segalanya, tapi sendiri
- Jika knowledge rendah: kebenaran tetap tertidur

THEME:
"Ketidakpedulian adalah kemenangan terbesar Gereja."
```

---

## 🎵 Anti-Patterns Dihindari

❌ **TIDAK ADANYA:**
- "Optimal play" atau "best choice" yang jelas
- Reward untuk menaikkan stat tanpa konsekuensi naratif
- Heroic language ("Anda menyelamatkan semua orang")
- Utopian endings ("Semuanya baik-baik saja")
- Stat display ke pemain
- Time limits yang eksplisit (implisit sahaja)

✅ **SEBALIKNYA:**
- Setiap pilihan membawa biaya tersembunyi
- Konsequences naratif yang berkembang secara halus
- Ending yang reflektif, bukan victorious
- Pemain belajar tentang timing melalui pengalaman, bukan tutorial
- "Waktu" adalah mekanik, bukan stat

---

## 🔄 Game Loop

**Single exit point untuk pengulangan:**
```python
def main():
    while True:
        start_game()
        # Tanyakan main lagi hanya setelah ending
        # Jika 'y', kembali ke `start_game()` dengan reset variabel
        # Jika 'n', exit()
```

---

## 📝 Design Choices Rationale

### 1. Mengapa Gradual vs Boolean?

Boolean `delayed_action` terlalu binary. `hesitation_level` memungkinkan:
- Pemain membuat beberapa pilihan pasif tapi tidak semua
- Narrative feedback yang scale dengan akumulasi, bukan tiba-tiba
- Threshold yang membuat sistem terasa "living" dan "responding"

### 2. Mengapa TRUE ENDING Sulit Dicapai?

Sesuai tema: keadilan yang sempurna LANGKA. Hanya possible dengan knowledge tinggi TAPI juga aksi lambat (high hesitation). Ini adalah konsekuensi, bukan reward untuk "playing smart".

### 3. Mengapa GOOD ENDING Perlu `hesitation_level <= 5`?

Keseimbangan antara action-oriented TAPI rational: tidak perlu terburu-buru, tapi juga tidak boleh menunggu terlalu lama. "Slow but steady" bukan "reckless".

### 4. Mengapa Coalition Penting?

Tanpa solidaritas sosial, bahkan pengetahuan + urgency tidak cukup. Ini mencerminkan realitas sejarah: gerakan sosial membutuhkan organisasi kolektif, bukan hanya kepemimpinan individual.

---

## 🎮 Player Agency

Pemain tidak tahu:
- Tentang `hesitation_level`
- Threshold ending
- Stat mereka (selain narasi)
- Jendela waktu yang tepat

Tapi mereka BISA:
- Melihat konsekuensi naratif (NPC hilang, aliansi ragu, warnings)
- Membuat keputusan berbeda dan mengalami hasil yang berbeda
- Merefleksikan tentang tradeoff antara knowledge, action, dan community

---

## 📚 Sources & Inspirations

- *Les Misérables* (Hugo): revolution membutuhkan waktu dan jasad
- *The Dispossessed* (Le Guin): institutional power vs individual choice
- *Complexity science*: tipping points dan irreversibility
- *Moral philosophy*: consequences of inaction = form of action

---

**Last Updated**: 2026-02-09  
**Status**: Full implementation complete with philosophical grounding
