import datetime
import os
import time

# Data akun
akun = {
    "admin": {"password": "2008", "role": "admin"},
    "user": {"password": "2008", "role": "user"}
}

# Data peralatan laboratorium
peralatan = {
    1: {
        "nama": "Mouse Logitech",
        "jenis": "Mouse",
        "kondisi": "Baik"
    },
    2: {
        "nama": "Keyboard Logitech",
        "jenis": "Keyboard",
        "kondisi": "Baik"
    },
    3: {
        "nama": "Mouse Rexus",
        "jenis": "Mouse",
        "kondisi": "Rusak"
    }
}


# Fungsi login
def login():
    print("=== LOGIN ===")
    username = input("Username : ")
    password = input("Password : ")

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil!")
        return username, akun[username]["role"]
    else:
        print("Username atau password salah!")
        return None, None


# Fungsi menampilkan data
def tampilkan_data():
    print("\n=== DATA PERALATAN LABORATORIUM ===")

    if len(peralatan) == 0:
        print("Belum ada data peralatan.")
    else:
        for nomor, data in peralatan.items():
            print(
                nomor, "|",
                data["nama"], "|",
                data["jenis"], "|",
                data["kondisi"]
            )


# Fungsi tambah data
def tambah_data():
    print("\n=== TAMBAH DATA PERALATAN ===")

    nama = input("Nama perangkat : ")
    jenis = input("Jenis (Mouse/Keyboard) : ")
    kondisi = input("Kondisi (Baik/Rusak) : ")

    if nama == "" or jenis == "" or kondisi == "":
        print("Data tidak boleh kosong!")
        return

    if jenis.lower() not in ["mouse", "keyboard"]:
        print("Jenis hanya boleh Mouse atau Keyboard!")
        return

    if kondisi.lower() not in ["baik", "rusak"]:
        print("Kondisi hanya boleh Baik atau Rusak!")
        return

    nomor = max(peralatan.keys(), default=0) + 1

    peralatan[nomor] = {
        "nama": nama,
        "jenis": jenis,
        "kondisi": kondisi
    }

    print("Data berhasil ditambahkan.")
    print("Tanggal :", datetime.date.today())


# Fungsi ubah data
def ubah_data():
    tampilkan_data()

    try:
        nomor = int(input("\nMasukkan nomor data yang diubah: "))

        if nomor not in peralatan:
            print("Nomor data tidak ditemukan!")
            return

        nama = input("Nama baru : ")
        jenis = input("Jenis baru : ")
        kondisi = input("Kondisi baru : ")

        if nama == "" or jenis == "" or kondisi == "":
            print("Data tidak boleh kosong!")
            return

        if jenis.lower() not in ["mouse", "keyboard"]:
            print("Jenis hanya boleh Mouse atau Keyboard!")
            return

        if kondisi.lower() not in ["baik", "rusak"]:
            print("Kondisi hanya boleh Baik atau Rusak!")
            return

        peralatan[nomor] = {
            "nama": nama,
            "jenis": jenis,
            "kondisi": kondisi
        }

        print("Data berhasil diubah.")

    except ValueError:
        print("Nomor harus berupa angka!")


# Fungsi hapus data
def hapus_data():
    tampilkan_data()

    try:
        nomor = int(input("\nMasukkan nomor data yang dihapus: "))

        if nomor in peralatan:
            del peralatan[nomor]
            print("Data berhasil dihapus.")
        else:
            print("Nomor data tidak ditemukan!")

    except ValueError:
        print("Nomor harus berupa angka!")


# Program utama
def main():
    while True:
        username, role = login()

        if username is not None:
            break

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("==========================================")
        print(" SISTEM PENDATAAN MOUSE DAN KEYBOARD")
        print("          LABORATORIUM")
        print("==========================================")
        print("Tanggal       :", datetime.date.today())
        print("Login sebagai :", role)

        print("\n1. Lihat Data")

        if role == "admin":
            print("2. Tambah Data")
            print("3. Ubah Data")
            print("4. Hapus Data")

        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tampilkan_data()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2" and role == "admin":
            tambah_data()
            time.sleep(1)

        elif pilihan == "3" and role == "admin":
            ubah_data()
            time.sleep(1)

        elif pilihan == "4" and role == "admin":
            hapus_data()
            time.sleep(1)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak valid!")
            time.sleep(1)


main()