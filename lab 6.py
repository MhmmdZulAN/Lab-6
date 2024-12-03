data_mahasiswa = []

#Menambahkan data mahasiswa
def tambah_data():
    nama = input("Masukkan nama: ")
    nilai = input("Masukkan nilai: ")
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("Data berhasil ditambahkan!")

#Menampilkan Data mahasiswa
def tampilkan_data():
    if len(data_mahasiswa) == 0:
        print("Tidak ada data.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, data in enumerate(data_mahasiswa):
            print(f"{i + 1}. Nama: {data['nama']}, Nilai: {data['nilai']}")

#Menghapus data
def hapus_data(nama):
    for data in data_mahasiswa:
        if data["nama"].lower() == nama.lower():
            data_mahasiswa.remove(data)
            print(f"Data dengan nama {nama} berhasil dihapus.")
            return
    print(f"Data dengan nama {nama} tidak ditemukan.")

#Mengubah data
def ubah_data(nama):
    for data in data_mahasiswa:
        if data["nama"].lower() == nama.lower():
            nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
            data["nilai"] = nilai_baru
            print(f"Data dengan nama {nama} berhasil diubah.")
            return
    print(f"Data dengan nama {nama} tidak ditemukan.")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dihapus: ")
        hapus_data(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang ingin diubah: ")
        ubah_data(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia. silahkan pilih yang lain.")
