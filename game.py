import random

# Global variables
knowledge = 0
urgency = 0
coalition = 0
hesitation_level = 0  # Accumulates every time player delays/waits
                       # 0-3: early delays, seems reasonable
                       # 4-6: visible consequences
                       # 7+: irreversible loss of collective action window

def start_game():
    """Menginisialisasi game dan mereset semua variabel"""
    global knowledge, urgency, coalition, hesitation_level
    knowledge = 0
    urgency = 0
    coalition = 0
    hesitation_level = 0
    
    print("\n" + "="*50)
    print("FIRMAMEN")
    print("="*50)
    print("\nSebuah dunia di bawah langit palsu.")
    print("Sebuah gereja dengan rahasia yang membara.")
    print("Waktu Anda untuk bertindak tidak terbatas... atau apakah begitu?\n")
    
    scene_1()

def scene_1():
    """Scene 1: Kelas Astronomi Matematika"""
    global knowledge, urgency, coalition, hesitation_level
    
    print("\n" + "="*50)
    print("SCENE 1: Kelas Astronomi Matematika")
    print("="*50)
    print("\nAnda memasuki ruangan kelas yang ramai dengan diskusi.")
    print("Profesor membahas pergerakan bintang dengan presisi matematis.")
    print("Ada ketegangan yang tegang antara dogma keagamaan dan data empiris.")
    print("\nBagaimana Anda merespons?")
    print("\n1. Membela kehendak Huitzilopochtli")
    print("2. Diam dan mengamati data")
    print("3. Menantang asumsi secara matematis")
    
    choice = input("\nPilihan Anda (1-3): ").strip()
    
    if choice == "1":
        urgency += 1
        coalition += 1
        print("\nAnda membela kehendak Huitzilopochtli dengan vokal.")
    elif choice == "2":
        knowledge += 2
        hesitation_level += 1  # Mulai menunda
        print("\nAnda memilih untuk diam dan mengamati data dengan seksama.")
        print("Tapi ada sesuatu dalam bola matanya profesor—keputusasaan.")
    elif choice == "3":
        knowledge += 3
        urgency -= 1
        print("\nAnda menantang asumsi dengan pertanyaan matematis yang tajam.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    scene_2()

def scene_2():
    """Scene 2: Membaca berkas Profesor Skemma"""
    global knowledge, urgency, coalition, hesitation_level
    
    print("\n" + "="*50)
    print("SCENE 2: Membaca Berkas Profesor Skemma")
    print("="*50)
    print("\nAnda menemukan berkas rahasia di perpustakaan.")
    print("Berkas tersebut berisi tabel terperinci tentang sudut bintang")
    print("dan koreksi berulang yang menunjukkan pola jelas melawan dogma resmi.")
    
    # Narrative feedback berdasarkan hesitation accumulation
    if hesitation_level >= 4:
        print("\nTapi sesuatu lebih mengganggu: tanggal dokumen menunjukkan")
        print("data ini sudah diketahui Gereja bertahun-tahun lalu.")
        print("Mereka memilih untuk membiarkan ritual pembakaran berlanjut.")
        print("\nAnda mencoba menghubungi Profesor Skemma, tapi dia hilang.")
    elif hesitation_level >= 1:
        print("\nAnda mencoba memahami mengapa data semacam ini")
        print("belum pernah dibagikan dengan dunia.")
    
    print("\nApa yang akan Anda lakukan?")
    print("\n1. Memverifikasi ulang semua data")
    print("2. Menghubungkan data dengan eksekusi publik")
    print("3. Menyimpan data dan melanjutkan observasi")
    
    choice = input("\nPilihan Anda (1-3): ").strip()
    
    if choice == "1":
        knowledge += 2
        urgency -= 1
        print("\nAnda dengan cermat memverifikasi ulang setiap data.")
    elif choice == "2":
        knowledge += 1
        coalition += 2
        print("\nAnda menyadari kaitan antara data dan eksekusi publik.")
    elif choice == "3":
        knowledge += 1
        urgency += random.randint(0, 1)
        hesitation_level += 2  # Pilihan menunggu lagi += lebih banyak
        print("\nAnda menyimpan data dan melanjutkan observasi.")
        
        if hesitation_level >= 6:
            print("Tindakan Gereja semakin agresif—lebih banyak penghukuman.")
            print("Anda dengar kabar bahwa dua aliansi Anda mulai ragu.")
        else:
            print("Tindakan Gereja terus berlanjut, tapi Anda percaya pada data Anda.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 1
    
    scene_3()

def scene_3():
    """Scene 3: Menentukan strategi menghadapi Gereja"""
    global knowledge, urgency, coalition, hesitation_level
    
    print("\n" + "="*50)
    print("SCENE 3: Menentukan Strategi Menghadapi Gereja")
    print("="*50)
    print("\nWaktu pengambilan keputusan telah tiba.")
    print("Anda harus memilih bagaimana mengkomunikasikan temuan kepada dunia,")
    print("berhadapan dengan tekanan Gereja yang semakin besar.")
    
    # Narrative escalation based on hesitation
    if hesitation_level >= 7:
        print("\n*** PERINGATAN TERSEMBUNYI ***")
        print("Aliansi Anda mulai runtuh. Orang-orang takut berbicara.")
        print("Beberapa bahkan meragukan apakah data itu nyata atau obsesi Anda.")
        print("Waktu untuk tindakan kolektif telah hampir berakhir.")
    elif hesitation_level >= 5:
        print("\nAnda dengar hari ini: tiga orang baru dieksekusi.")
        print("Alasan mereka yang diberitahu: 'Kecurigaan pada bintang.'")
        print("Aliansi Anda menunggu kepemimpinan.")
    else:
        print("\nAnda masih memiliki kepercayaan dari komunitas.")
        print("Mereka menunggu keputusan Anda.")
    
    print("\nStrategi mana yang akan Anda pilih?")
    print("\n1. Mempublikasikan data mentah ke publik")
    print("2. Membangun narasi kemanusiaan")
    print("3. Menunggu konsistensi data yang sempurna")
    
    choice = input("\nPilihan Anda (1-3): ").strip()
    
    if choice == "1":
        knowledge += 1
        urgency += 2
        coalition += random.randint(0, 1)
        print("\nAnda memutuskan untuk mempublikasikan data mentah.")
    elif choice == "2":
        coalition += 3
        urgency += 1
        print("\nAnda membangun narasi kemanusiaan yang kuat.")
    elif choice == "3":
        knowledge += 2
        urgency -= 2
        hesitation_level += 3  # Pilihan menunggu paling berat
        print("\nAnda memilih untuk menunggu konsistensi data yang sempurna.")
        
        if hesitation_level >= 8:
            print("\nSambil Anda menunggu, lebih banyak orang menghilang.")
            print("Beberapa aliansi Anda memilih untuk mundur—terlalu lama.")
            coalition -= random.randint(1, 2)  # Kehilangan aliansi
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    scene_4()

def scene_4():
    """Scene 4: Titik tidak bisa kembali"""
    global knowledge, urgency, coalition, hesitation_level
    
    print("\n" + "="*50)
    print("SCENE 4: Titik Tidak Bisa Kembali")
    print("="*50)
    print("\nDunia mulai menunjukkan tanda ketidakstabilan.")
    print("Cahaya patung Huitzilopochtli tidak konsisten, berkedip-kedip.")
    print("Anda menyadari bahwa sistem yang mempertahankan ilusi runtuh.")
    
    # Critical narrative branch based on hesitation_level
    if hesitation_level >= 8:
        print("\n*** TITIK TIDAK BISA KEMBALI TELAH TERLAMPAUI ***")
        print("Waktu Anda untuk mobilisasi aksi kolektif sudah hilang.")
        print("Aliansi Anda telah bercerai. Banyak yang sudah mati.")
        print("Dunia akan berubah, tetapi Anda akan menjadi saksi—bukan pemimpin.")
    elif hesitation_level >= 6:
        print("\n*** PERINGATAN NARATIF ***")
        print("Waktu Anda untuk tindakan kolektif hampir usai.")
        print("Aliansi Anda mulai kehilangan kepercayaan diri.")
        print("Satu pilihan tidak tepat lagi dan Anda kehilangan segalanya.")
    else:
        print("\nAnda masih memiliki aliansi dan kepercayaan dari komunitas.")
        print("Jendela waktu untuk tindakan kolektif masih terbuka.")
    
    print("\nApa yang akan Anda lakukan dalam momen kritis ini?")
    print("\n1. Bertindak cepat terhadap patung")
    print("2. Mengkoordinasikan aksi bertahap lintas kelompok")
    print("3. Menunggu sampai semua argumen lengkap")
    
    choice = input("\nPilihan Anda (1-3): ").strip()
    
    if choice == "1":
        urgency += 3
        knowledge -= 1
        print("\nAnda bertindak cepat terhadap patung.")
    elif choice == "2":
        coalition += 3
        urgency += 1
        print("\nAnda mengkoordinasikan aksi bertahap lintas kelompok.")
    elif choice == "3":
        knowledge += 2
        urgency -= 3
        hesitation_level += 3  # Final wait—too late
        print("\nAnda memilih untuk menunggu sampai semua argumen lengkap.")
        
        if hesitation_level >= 10:
            print("\nTapi waktu sudah habis. Sistem runtuh dengan cara sendiri,")
            print("dan Anda hanya bisa menyaksikan.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    check_ending()

def check_ending():
    """
    Menentukan ending berdasarkan distribusi keputusan, bukan optimasi stat.
    
    Thesis: Kebenaran tanpa tindakan tepat waktu adalah kerugian.
    Urgency, knowledge, dan coalition harus diikuti dengan tatanan yang benar.
    """
    global knowledge, urgency, coalition, hesitation_level
    
    print("\n" + "="*50)
    print("ENDING")
    print("="*50 + "\n")
    
    # Narasi universal pembuka
    print("Cahaya patung itu bersinar sekali lagi—lalu gelap sama sekali.\n")
    
    # TRUE ENDING: Knowledge tinggi + Hesitation tinggi + Aksi kolektif gagal
    # Artinya: pemain tahu segalanya, tapi aksi kolektif sudah terlalu lambat
    # Dunia eventually runtuh, kebenaran terungkap, tapi korban sudah jatuh
    if knowledge >= 6 and hesitation_level >= 7 and coalition < 5:
        print("KEBENARAN YANG TERLAMBAT")
        print("-" * 30)
        print("\nLangit palsu terdisintegrasi dengan sendirinya—")
        print("mekanisme internalnya runtuh seperti rumah kartu.")
        print("\nDunia akhirnya mengetahui kebenaran.")
        print("Semua data Anda ternyata benar.")
        print("\nTapi ribuan sudah meninggal di depan patung itu.")
        print("Aliansi Anda tercerai sebelum bisa berbuat apa pun.")
        print("\nAnda memiliki jawaban untuk semuanya.")
        print("Tetapi Anda tidak memiliki suara untuk menyuarakan kepada siapa pun")
        print("yang masih hidup untuk mendengarkan.")
        print("\n[Pengetahuan tanpa ketepatan waktu adalah bentuk kebohongan lain.]")
    
    # GOOD ENDING: Keseimbangan—urgency + coalition tinggi, hesitation rendah
    # Sky runtuh perlahan, ada resistance, tapi komunitas bergerak bersama
    elif knowledge >= 5 and urgency >= 5 and coalition >= 5 and hesitation_level <= 5:
        print("LANGIT YANG REWEL")
        print("-" * 30)
        print("\nLangit palsu tidak langsung runtuh.")
        print("Ia terdisintegrasi perlahan-lahan, bagian demi bagian.")
        print("\nGereja melawan dengan semua yang mereka miliki,")
        print("tetapi koalisi Anda bertahan di antara kekacauan.")
        print("\nOrang-orang mulai melihat ribuan bintang asli")
        print("untuk pertama kalinya dalam generasi mereka.")
        print("\nTapi ada bekas luka.")
        print("Kepercayaan terhadap institusi hancur berkeping-keping.")
        print("Sebagian akan membutuhkan bertahun-tahun untuk pulih.")
        print("\nTetapi Anda berhasil. Tidak sempurna. Tidak bersih.")
        print("Tetapi bersama, Anda memilih untuk bertindak.")
        print("\n[Kemenangan yang berdebu lebih bermakna daripada keputusan sempurna yang terpurbait.]")
    
    # BAD ENDING: Semua skenario lainnya
    # Gereja bertahan, ilusi terus berlanjut
    else:
        print("GEREJA BERTAHAN")
        print("-" * 30)
        print("\nGereja berhasil mempertahankan kontrol.")
        print("Ritual pembakaran berlanjut di bawah patung yang masih bersinar.")
        print("Langit palsu tetap utuh di atas kepala generasi berikutnya.")
        
        if knowledge >= 6:
            print("\nAnda memiliki jawaban. Tetapi Anda berdiri sendiri.")
            print("Kebenaran hanya bernilai jika ada orang yang mendengarkan.")
            print("Dan waktu Anda untuk membuat orang mendengarkan—sudah hilang.")
        else:
            print("\nKebenaran tetap tertidur di bawah lapisan kebohongan.")
            print("Ilusi terus berlanjut karena mereka yang tahu terlalu terlambat,")
            print("dan mereka yang berbuat terlalu lemah.")
        
        print("\n[Ketidakpedulian adalah kemenangan terbesar Gereja.]")
    
    return True


def main():
    """Main game loop dengan satu mekanisme repetisi"""
    while True:
        start_game()
        
        # Tanyakan apakah ingin main lagi
        print("\n" + "="*50)
        while True:
            play_again = input("\nMain lagi? (y/n): ").strip().lower()
            if play_again == 'y':
                break
            elif play_again == 'n':
                print("\nTerima kasih telah bermain.")
                print("Suara Anda untuk kebenaran—apakah Anda akan menggunakannya tepat waktu?")
                print("="*50 + "\n")
                exit()
            else:
                print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()
