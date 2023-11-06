"""
Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara sekuensial. 
Apa maksudnya? Kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. 
Aksi sekuensial sendiri memiliki makna sebagai sederetan instruksi yang akan dijalankan oleh 
komputer berdasarkan urutan penulisannya.
"""


print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
 
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")