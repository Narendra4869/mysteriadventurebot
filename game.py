import random

# Global variables
knowledge = 0
urgency = 0
coalition = 0

def start_game():
    """Menginisialisasi game dan mereset semua variabel"""
    global knowledge, urgency, coalition
    knowledge = 0
    urgency = 0
    coalition = 0
    
    print("\n" + "="*50)
    print("Firmamen")
    print("="*50 + "\n")
    
    scene_1()

def scene_1():
    """Scene 1: Kelas Astronomi Matematika"""
    global knowledge, urgency, coalition
    
    print("="*50)
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
        print("\nAnda memilih untuk diam dan mengamati data dengan seksama.")
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
    global knowledge, urgency, coalition
    
    print("\n" + "="*50)
    print("SCENE 2: Membaca Berkas Profesor Skemma")
    print("="*50)
    print("\nAnda menemukan berkas rahasia di perpustakaan.")
    print("Berkas tersebut berisi tabel terperinci tentang sudut bintang")
    print("dan koreksi berulang yang menunjukkan pola jelas melawan dogma resmi.")
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
        print("\nAnda menyimpan data dan melanjutkan observasi.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 1
    
    scene_3()

def scene_3():
    """Scene 3: Menentukan strategi menghadapi Gereja"""
    global knowledge, urgency, coalition
    
    print("\n" + "="*50)
    print("SCENE 3: Menentukan Strategi Menghadapi Gereja")
    print("="*50)
    print("\nWaktu pengambilan keputusan telah tiba.")
    print("Anda harus memilih bagaimana mengkomunikasikan temuan kepada dunia,")
    print("berhadapan dengan tekanan Gereja yang semakin besar.")
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
        print("\nAnda memilih untuk menunggu konsistensi data yang sempurna.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    scene_4()

def scene_4():
    """Scene 4: Titik tidak bisa kembali"""
    global knowledge, urgency, coalition
    
    print("\n" + "="*50)
    print("SCENE 4: Titik Tidak Bisa Kembali")
    print("="*50)
    print("\nDunia mulai menunjukkan tanda ketidakstabilan.")
    print("Cahaya patung Huitzilopochtli tidak konsisten, berkedip-kedip.")
    print("Anda menyadari bahwa sistem yang mempertahankan ilusi runtuh.")
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
        print("\nAnda memilih untuk menunggu sampai semua argumen lengkap.")
    else:
        print("\nPilihan tidak valid. Menggunakan pilihan default.")
        knowledge += 2
    
    check_ending()

def check_ending():
    """Menentukan dan menampilkan ending berdasarkan nilai stat"""
    global knowledge, urgency, coalition
    
    print("\n" + "="*50)
    print("ENDING")
    print("="*50 + "\n")
    
    # TRUE ENDING: knowledge >= 7 dan urgency <= 3
    if knowledge >= 7 and urgency <= 3:
        print("LANGIT ASLI TERSINGKAP")
        print("-" * 30)
        print("\nEnergi yang mempertahankan ilusi lenyap mendadak.")
        print("Langit palsu runtuh dengan cepat seperti kaca yang pecah.")
        print("Tapi Anda terlambat—ritual pembakaran tidak sempat dihentikan.")
        print("\nDengan pengetahuan sempurna namun tindakan minimal,")
        print("Anda saksikan transformasi dunia dengan matang dan bijak.")
    
    # GOOD ENDING: knowledge >= 6 dan urgency >= 5 dan coalition >= 5
    elif knowledge >= 6 and urgency >= 5 and coalition >= 5:
        print("KEBEBASAN BERSAMA")
        print("-" * 30)
        print("\nLangit palsu terdisintegrasi perlahan-lahan.")
        print("Penduduk melihat langit asli untuk pertama kalinya.")
        print("Matahari nyata bersinar di atas kerajaan yang telah dibebaskan.")
        print("\nKoalisi lintas kelompok Anda berhasil membangun masa depan baru,")
        print("di mana kebenaran dan kemanusiaan berjalan beriringan.")
    
    # BAD ENDING: selainnya
    else:
        print("GEREJA BERTAHAN")
        print("-" * 30)
        print("\nGereja berhasil mempertahankan kontrol.")
        print("Ritual pembakaran berlanjut di bawah patung yang masih bersinar.")
        print("Langit palsu tetap utuh di atas kepala generasi berikutnya.")
        print("\nKebenaran tetap tertidur, dan ilusi terus berlanjut...")
    
    # Tanyakan apakah ingin main lagi
    print("\n" + "="*50)
    while True:
        play_again = input("\nMain lagi? (y/n): ").strip().lower()
        if play_again == 'y':
            start_game()
            break
        elif play_again == 'n':
            print("\nTerima kasih telah bermain. Sampai jumpa!")
            print("="*50 + "\n")
            exit()
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

def main():
    """Main game loop"""
    while True:
        start_game()

if __name__ == "__main__":
    main()
