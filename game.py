import random

# Global variables
knowledge = 0
urgency = 0
coalition = 0
delayed_action = False  # Track jika pemain sering memilih untuk menunggu/diam

def start_game():
    """Menginisialisasi game dan mereset semua variabel"""
    global knowledge, urgency, coalition, delayed_action
    knowledge = 0
    urgency = 0
    coalition = 0
    delayed_action = False
    
    print("\n" + "="*50)
    print("FIRMAMEN")
    print("="*50)
    print("\nSebuah dunia di bawah langit palsu.")
    print("Sebuah gereja dengan rahasia yang membara.\n")
    
    scene_1()

def scene_1():
    """Scene 1: Kelas Astronomi Matematika"""
    global knowledge, urgency, coalition, delayed_action
    
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
        delayed_action = True  # Pilihan pasif pertama
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
    global knowledge, urgency, coalition, delayed_action
    
    print("\n" + "="*50)
    print("SCENE 2: Membaca Berkas Profesor Skemma")
    print("="*50)
    print("\nAnda menemukan berkas rahasia di perpustakaan.")
    print("Berkas tersebut berisi tabel terperinci tentang sudut bintang")
    print("dan koreksi berulang yang menunjukkan pola jelas melawan dogma resmi.")
    
    if delayed_action:
        print("\nTapi sesuatu lebih mengganggu: tanggal dokumen menunjukkan")
        print("data ini sudah diketahui Gereja bertahun-tahun lalu.")
        print("Mereka memilih untuk membiarkan ritual pembakaran berlanjut.")
    
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
        delayed_action = True  # Pilihan pasif lagi
        print("\nAnda menyimpan data dan melanjutkan observasi.")
        print("Tindakan Gereja semakin agresif—lebih banyak penghukuman.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 1
    
    scene_3()

def scene_3():
    """Scene 3: Menentukan strategi menghadapi Gereja"""
    global knowledge, urgency, coalition, delayed_action
    
    print("\n" + "="*50)
    print("SCENE 3: Menentukan Strategi Menghadapi Gereja")
    print("="*50)
    print("\nWaktu pengambilan keputusan telah tiba.")
    print("Anda harus memilih bagaimana mengkomunikasikan temuan kepada dunia,")
    print("berhadapan dengan tekanan Gereja yang semakin besar.")
    
    if delayed_action:
        print("\nAnda dengar hari ini: tiga orang baru dieksekusi.")
        print("Alasan mereka yang diberitahu: 'Kecurigaan pada bintang.'")
    
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
        delayed_action = True  # Pilihan tungggu lagi
        print("\nAnda memilih untuk menunggu konsistensi data yang sempurna.")
        print("Sambil Anda menunggu, penjara Gereja penuh.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    scene_4()

def scene_4():
    """Scene 4: Titik tidak bisa kembali"""
    global knowledge, urgency, coalition, delayed_action
    
    print("\n" + "="*50)
    print("SCENE 4: Titik Tidak Bisa Kembali")
    print("="*50)
    print("\nDunia mulai menunjukkan tanda ketidakstabilan.")
    print("Cahaya patung Huitzilopochtli tidak konsisten, berkedip-kedip.")
    print("Anda menyadari bahwa sistem yang mempertahankan ilusi runtuh.")
    
    if delayed_action:
        print("\n*** PERINGATAN NARATIF ***")
        print("Waktu Anda untuk tindakan kolektif hampir habis.")
        print("Setiap pilihan menunggu membawa Anda lebih dekat ke titik tanpa")
        print("kemampuan menyelamatkan apa pun selain pengetahuan murni.")
        print("***")
    else:
        print("\nAnda masih memiliki aliansi dan kepercayaan dari komunitas.")
    
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
        delayed_action = True  # Pilihan terakhir untuk menunggu
        print("\nAnda memilih untuk menunggu sampai semua argumen lengkap.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    check_ending()

def check_ending():
    """Menentukan dan menampilkan ending berdasarkan nilai stat dan keputusan pemain"""
    global knowledge, urgency, coalition, delayed_action
    
    print("\n" + "="*50)
    print("ENDING")
    print("="*50 + "\n")
    
    # Refleksi naratif sebelum ending (tanpa expose stat)
    print("Cahaya patung itu bersinar sekali lagi—lalu gelap sama sekali.\n")
    
    # TRUE ENDING: knowledge >= 7 dan urgency <= 3 TETAPI not delayed_action
    # Ini memastikan TRUE ENDING hanya tercapai dengan tindakan proaktif, bukan pasif
    if knowledge >= 7 and urgency <= 3 and not delayed_action:
        print("LANGIT ASLI TERSINGKAP")
        print("-" * 30)
        print("\nEnergi yang mempertahankan ilusi lenyap mendadak.")
        print("Langit palsu runtuh dengan cepat seperti kaca yang pecah.")
        print("\nTapi Anda terlambat—ritual pembakaran tidak sempat dihentikan.")
        print("Korban terakhir sudah jatuh sebelum cahaya itu padam.")
        print("\nDengan pengetahuan sempurna namun tindakan di saat yang tepat,")
        print("Anda saksikan transformasi dunia dengan matang dan bijak.")
        print("\n[Kebenaran menang, tetapi dengan harga yang tragis.]")
    
    # TRUE ENDING (alternatif): knowledge tinggi BUT delayed_action = True
    # Ini adalah TRUE ENDING yang lebih benar-benar tragis (knowledge tanpa aksi)
    elif knowledge >= 7 and delayed_action:
        print("PENGETAHUAN TANPA SUARA")
        print("-" * 30)
        print("\nLangit palsu terdisintegrasi, tetapi bukan karena tindakan Anda.")
        print("Sistem runtuh oleh mekanisme internalnya sendiri, terlalu terlambat.")
        print("\nAnda memiliki semua jawaban. Tetapi jawaban itu hanya milik Anda.")
        print("Gereja sudah mencegah siapa pun mendengarkannya.")
        print("\nDunia berubah, tetapi Anda berdiri sendirian sebagai saksi,")
        print("tidak sebagai pembebas.")
        print("\n[Kebenaran ada. Tetapi keadilan tidak datang bersamanya.]")
    
    # GOOD ENDING: knowledge >= 6 dan urgency >= 5 dan coalition >= 5
    elif knowledge >= 6 and urgency >= 5 and coalition >= 5:
        print("KEBEBASAN BERSAMA")
        print("-" * 30)
        print("\nLangit palsu terdisintegrasi perlahan-lahan.")
        print("Penduduk melihat langit asli untuk pertama kalinya.")
        print("Matahari nyata bersinar di atas kerajaan yang telah dibebaskan.")
        print("\nKoalisi lintas kelompok Anda berhasil membangun masa depan baru,")
        print("di mana kebenaran dan kemanusiaan berjalan beriringan.")
        print("\n[Pengetahuan + Tindakan + Solidaritas = Perubahan yang berkelanjutan.]")
    
    # BAD ENDING: selainnya
    else:
        print("GEREJA BERTAHAN")
        print("-" * 30)
        print("\nGereja berhasil mempertahankan kontrol.")
        print("Ritual pembakaran berlanjut di bawah patung yang masih bersinar.")
        print("Langit palsu tetap utuh di atas kepala generasi berikutnya.")
        print("\nKebenaran—jika Anda temukannya—tetap rahasia Anda sendiri.")
        print("Ilusi terus berlanjut karena mereka yang tahu tidak berbuat,")
        print("dan mereka yang berbuat terlalu sedikit, terlalu lambat.")
        print("\n[Ketidakpedulian adalah kemenangan terbesar Gereja.]")
    
    return True  # Sinyal untuk main_loop bahwa sudah finish satu game


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
                print("Suara Anda untuk kebenaran—kapan pun waktunya.")
                print("="*50 + "\n")
                exit()
            else:
                print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()
