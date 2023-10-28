# Fungsi untuk memeriksa usia pemilih
def cek_usia_pemilih():
    print("Selamat datang di Sistem Pemilu")
    while True:
        try:
            usia = int(input("Masukkan usia Anda: "))
            global minimal_usia
            if usia >= 17:
                minimal_usia = True
                print("\nAnda memenuhi syarat untuk memilih dalam pemilu.\n")
            else:
                minimal_usia = False
                print("\nMaaf, Anda belum cukup usia untuk memilih.\n")
            break
        except ValueError:
            print("Masukkan angka yang valid.")

# Fungsi untuk memeriksa status keanggotaan partai politik
def cek_keanggotaan_partai():
    print("Selamat datang di Sistem Pemilu")
    daftar_parpol = ["PDIP", "Golkar", "Gerindra", "Demokrat", "PAN", "PSI", "PPP", "Nasdem", "Perindo"]
    partai = input("Apakah Anda anggota partai politik? (ya/tidak): ")
    if partai == 'ya':
        print("Berikut ini adalah daftar partai politik")
        for i in daftar_parpol:
            print (i)
        partai_penduduk = input("Silakan masukkan partai politik Anda : ")
        if partai_penduduk in daftar_parpol:
            print("Anda memiliki hal untuk memilih dalam pemilihan partai")
        else:
            print("Anda dapat memilih calon independen dalam pemilu")
    else:
        print("Anda dapat memilih calon independen dalam pemilu.")

# Fungsi untuk memeriksa pemilih terdaftar atau tidak
def cek_pemilih_terdaftar():
    cek_usia_pemilih()
    print("Selamat Datang di Sistem Pemilu!")
    daftar_pemilih = ["Lisa", "Isa", "Maliki", "Rahma", "Wati", "Naruto", "Anime"]
    nama = input("Masukkan nama Anda: ")
    if nama in daftar_pemilih:
        pemilih = True
        print("\nAnda terdaftar sebagai pemilih.\n")
    else:
        pemilih = False
        print("\nMaaf, Anda tidak terdaftar sebagai pemilih.\n")

    print("Kesimpulannya adalah")
    if minimal_usia == True and pemilih == True:
        print("Anda berhak mengikuti Pemilihan Umum")
    else:
        print("Anda tidak berhak mengikuti Pemilihan Umum")

# Main program
while True:
    print("\nPilih Operasi:")
    print("1. Cek Hak Pilih Anda")
    print("2. Cek Keanggotaan Partai Politik")
    print("3. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == '1':
        cek_pemilih_terdaftar()
    elif pilihan == '2':
        cek_keanggotaan_partai()
    elif pilihan == '3':
        print("Terima kasih! Sampai jumpa lagi.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")