"""
Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan 
dan di mana harus memulai dan berakhir. Pada materi sebelumnya, Anda telah mempelajari aksi sekuensial. 
Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.

Dalam Python, program dapat berupa blok kode. Python sangat memperhatikan indentasi untuk membangun 
sebuah blok kode. Salah satu blok pemrograman adalah perulangan. Perulangan adalah satu dari beberapa 
control flow. 

Control flow memungkinkan program untuk berjalan berdasarkan jalur eksekusi. Control flow terbagi 
menjadi beberapa jenis, yakni kondisi tertentu (percabangan), mengulang blok kode secara berulang (perulangan),
melewati sebagian kode dan berhenti di kode tertentu, hingga mendefinisikan fungsi. 
"""

"""
#TODO CONTOH
Misalnya dalam keadaan seperti berikut.

1. Jika Anda tidak menyelesaikan kelas Memulai Pemrograman dengan Python, maka Anda tidak lulus dari 
   kelas Memulai Pemrograman dengan Python.
2. Jika jumlah variabel nama kurang dari dua, maka variabel tersebut tidak memenuhi kriteria kondisi.
"""

# Cara umum
print("===== Cara Umam =====")
belajar = "Python"

if belajar == "Python":
    print("Selamat anda lulus")
else:
    print("Maaf Belajar lebih giat lagi ya")
    
# Cara one-linear
print("===== One-linear =====")
if belajar == "Python": print("Selamat anda lulus")

# Contoh soal 1 (else if)
"""
- Buatlah variable tinggi_badan dengan nilai 160
- Jika tinggi badan kamu dibawah 160 maka kamu tidak diperbolekan untuk menaiki roller coaster dan sebaliknya
"""
print("===== Soal tinggi badan =====")
tinggi_badan = 160

if tinggi_badan >= 120:
    print("Maaf kamu tidak diperbolehkan untuk menaiki roller coaster")
else:
    print("Silahkan untuk bisa menaiki roller coaster")


# Contoh soal 2 (elif)
"""
- Buatlah variable nilai dengan nilai 65
- Jika nilai kamu di atas 80 maka kamu mendapatkan nilai A
- Jika nilai kamu di atas 70 maka kamu mendapatkan nilai B
- Jika nilai kamu di atas 60 maka kamu mendapatkan nilai C

"""
print("===== Soal Nilai =====")
nilai = 65

if nilai >= 80:
    print("Selamat! anda mendapat nilai A")
    print("Pertahankan")
elif nilai >= 70:
    print("Hore! anda mendapat nilai B")
    print("Tingkatkan")
elif nilai >= 60:
    print("Hmm! anda mendapat nilai C")
    print("Ayo Semangatt")
else:
    print("Waduh, Kamu mendapat nilai D")
    print("Belajar lebih giat lagi ya")
    
# Contoh Soal Terakhir
"""
- Buat variable value dengan nilai 81 dan juga variable perilaku denga string "tidak baik"
- Jika value diatas 80 AND perilakunya baik maka Nilai kamu A dan berperilaku baik
- Jika value diatas 80 AND perilakunya tidak baik maka Nilai kamu A tapi tidak berperilaku baik
"""
print("===== Soal Nilai & Perilaku =====")
value = 81
perilaku = 'tidak baik'

if value>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif value>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")