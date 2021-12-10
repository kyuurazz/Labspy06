Data_Mahasiswa = {} 

def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()

def tidakAdaData(): 
    header()          
    print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()

def tambah():
    print("Tambah Data")
    nama       = input("Nama        : ")
    nim        = input("NIM         : ")
    nilaiTugas = int(input("Nilai Tugas : "))
    nilaiUTS   = int(input("Nilai UTS   : "))
    nilaiUAS   = int(input("Nilai UAS   : "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
    Data_Mahasiswa[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!")

def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
    else:
        no = 0
        header()
        for data in Data_Mahasiswa.items():
            no += 1 
            print(f"| {no:>2} | {data[1][0]:<7} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")               
        garis() 

def ubah():
    print("Ubah Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()

    else:
        nama = input("Masukan Nama : ") 
        if nama in Data_Mahasiswa.keys():
            print(f"Data ditemukan!")
            print(25*"=")
            print(f"Nama        : {nama}")
            print(f"NIM         : {Data_Mahasiswa[nama][0]}")
            print(f"Nilai Tugas : {Data_Mahasiswa[nama][1]}")
            print(f"Nilai UTS   : {Data_Mahasiswa[nama][2]}")
            print(f"Nilai UAS   : {Data_Mahasiswa[nama][3]}")
            print(25*"=")
            print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
            tanya = int(input("Apa yang ingin diubah? [1-3] : "))
            if tanya == 1:
                _nama = input("Masukan Nama Baru : ")
                Data_Mahasiswa[_nama] = Data_Mahasiswa.pop(nama)
                print("Berhasil merubah Nama! ")

            elif tanya == 2:
                _nim = input("Masukan Nim Baru : ")
                Data_Mahasiswa[nama][0] = _nim
                print("Berhasil merubah NIM!")

            elif tanya == 3:
                _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
                _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
                _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
                _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
                Data_Mahasiswa[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
                print("Berhasil merubah data nilai!")
            elif tanya == 0:
                pass
            
            else:
                print(f"Pilihan {tanya} tidak ada! Silahkan masukan [1-3]")

        else:
            print(f"Data {nama} tidak ditemukan!") 

def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()

    else:
        nama = input("Masukan nama : ")
        if(nama in Data_Mahasiswa):
            del Data_Mahasiswa[nama]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print(f"Data {nama} tidak ditemukan!")

loop = True
while loop:
    print()
    print(71*"-")
    print(25*"-", "Program Input Nilai", 25*"-")
    print(71*"-")
    print("1. Tambah Data \n2. Lihat Data \n3. Ubah Data \n4. Hapus Data \n0. Keluar")
    print(71*"-")
    menu = int(input("Pilih menu : "))
    print(71*"-")
    print()

    if menu == 1:
        tambah()       

    elif menu == 2:
        lihat()

    elif menu == 3:
        ubah() 

    elif menu == 4:
        hapus()

    elif menu == 0:
        print("Program selesai, Terima Kasih")
        loop = False 

    else:
        print(f"Menu '{menu}' tidak ada! Silahkan masukan [0-4]")