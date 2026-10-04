Nama   : Muhammad Raffy Putra Triadi
Nim    : 2609116091
Kelas  : C

<img width="960" height="540" alt="Screenshot 2026-10-04 204916" src="https://github.com/user-attachments/assets/14c07a4c-f1c3-4c77-8d45-5b52e0da891c" />
<img width="960" height="540" alt="Screenshot 2026-10-04 204930" src="https://github.com/user-attachments/assets/7fe644d1-4ac7-460f-90ec-2ea6c68492c0" />
<img width="960" height="540" alt="Screenshot 2026-10-04 204945" src="https://github.com/user-attachments/assets/a8936db4-5d91-4e59-8eda-da04bbd66d18" />
<img width="960" height="540" alt="Screenshot 2026-10-04 205002" src="https://github.com/user-attachments/assets/1753a505-6b7b-4bf3-953a-6632b5d3bf1d" />
<img width="960" height="540" alt="Screenshot 2026-10-04 205015" src="https://github.com/user-attachments/assets/87be52ae-ad73-4f21-b1da-a7ec56952385" />
<img width="960" height="540" alt="Screenshot 2026-10-04 205029" src="https://github.com/user-attachments/assets/e07e9b52-8de8-4171-ac24-c753e57d19a6" />
<img width="960" height="540" alt="Screenshot 2026-10-04 205041" src="https://github.com/user-attachments/assets/60d85476-8f51-4d27-8fdf-f47484d9ae7b" />
Program ini dibuat untuk mendata mouse dan keyboard yang ada di laboratorium. Di awal program terdapat datetime, os, dan PrettyTable. datetime digunakan untuk menampilkan tanggal, os digunakan untuk membersihkan tampilan terminal, sedangkan PrettyTable digunakan untuk membuat tampilan data menjadi lebih rapi.
Program ini mempunyai dua akun, yaitu admin dan user. Sebelum masuk ke menu utama, pengguna harus melakukan login terlebih dahulu. Jika username dan password benar, maka akan muncul pesan login berhasil. Setelah itu program akan mengecek role pengguna. Admin mempunyai akses yang lebih lengkap, sedangkan user hanya bisa melihat data.
Data perangkat disimpan menggunakan Dictionary. Data tersebut berisi nama perangkat, jenis perangkat, dan kondisi perangkat. Contohnya seperti Mouse Logitech, Keyboard Logitech, dan Mouse Rexus. Data ini nantinya bisa ditambah, diubah, atau dihapus oleh admin.
Pada bagian tampil data, program menampilkan semua perangkat yang sudah tersimpan. Saya menggunakan PrettyTable supaya hasilnya lebih rapi dan mudah dilihat. Admin juga bisa menambahkan data baru dengan memasukkan nama perangkat, jenis, dan kondisi. Sebelum disimpan, program mengecek apakah input tidak kosong dan jenis perangkat yang dimasukkan sesuai.
Untuk mengubah data, admin memilih nomor data yang ingin diubah lalu memasukkan data yang baru. Sedangkan pada menu hapus, admin memilih nomor data yang ingin dihapus. Kalau nomor yang dimasukkan tidak ada, program akan memberikan pesan bahwa data tidak ditemukan.
Program juga menggunakan try-except pada bagian input nomor data. Jadi kalau pengguna memasukkan huruf, program tidak langsung berhenti karena error, tetapi akan menampilkan pesan “Nomor harus berupa angka!”.
Untuk akun user, aksesnya hanya untuk melihat data dan keluar dari program. User tidak bisa melakukan tambah, ubah, atau hapus data. Jadi pembagian role ini digunakan untuk membedakan hak akses antara admin dan user.
program ini digunakan untuk mempermudah pendataan perangkat laboratorium. Program sudah menggunakan Dictionary, Function, login, dua role, validasi input, error handling, dan beberapa library Python.


<img width="958" height="505" alt="Screenshot 2026-10-04 205907" src="https://github.com/user-attachments/assets/a8173ba2-582a-47e8-93dc-910700e5fc03" />
Alur flowchart pada program ini mulai dari Start, kemudian pengguna masuk ke bagian login dengan memasukkan username dan password. Setelah itu sistem mengecek apakah data login yang dimasukkan benar. Jika salah, pengguna akan kembali ke bagian login untuk memasukkan data lagi. Jika benar, sistem akan mengecek role pengguna, apakah sebagai admin atau user.
Jika yang login adalah admin, maka akan masuk ke Menu Admin. Admin memiliki akses yang lebih lengkap, yaitu dapat menambah data, menampilkan data, mengubah data, menghapus data, dan logout. Setelah admin melakukan salah satu proses pengelolaan data, program akan kembali lagi ke menu admin sehingga admin masih bisa memilih menu lainnya. Jika admin memilih logout, maka proses akan berakhir.
Sedangkan jika yang login adalah user, pengguna akan masuk ke Menu User. Pada bagian ini user hanya memiliki akses untuk melihat data dan logout. User tidak dapat menambah, mengubah, atau menghapus data. Setelah melihat data, program akan kembali ke menu user. Jika memilih logout, program akan menuju ke bagian akhir.
Jadi, secara keseluruhan alurnya adalah Start → Login → pengecekan username dan password → pengecekan role → masuk ke menu Admin atau User → melakukan proses sesuai hak akses → Logout → Selesai. Pembagian role ini dibuat supaya admin bisa mengelola seluruh data perangkat, sedangkan user hanya bisa melihat data yang sudah tersedia.
