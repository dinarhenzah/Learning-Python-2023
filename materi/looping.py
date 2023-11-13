
#===== Looping =====#

# For
# Menggunakan variable list untuk dilooping
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

print("========== Batas ===========")
# Menggunakan range(start,stop,step)
for i in range(1,10,2):
    print(i)
    
print("========== While ===========")
# While merupakan ekspresi yang akan dievaluasi dan menghasilkan nilai true atau false. 
# Selama hasil evaluasi bernilai true, program akan terus berjalan hingga menghasilkan nilai false.
nilai = 1
while nilai <= 5:
    print(nilai)
    nilai += 2
    
print("========== For Bersarang/Nested loop ===========")
# Nested Loop
"""
Anda dapat asumsikan bahwa ada dua perulangan, yakni "perulangan luar" dan "perulangan dalam". 
Program akan melakukan "perulangan luar" terlebih dahulu, lalu akan melakukan "perulangan dalam". 
"variabel_luar" akan mengambil nilai dari "iterable_luar", sedangkan "variabel_dalam" akan mengambil 
nilai dari "iterable_dalam".
"""
for i in (1,2):         # <- outer loop
    for j in (1,2):     # <- inner loop
        print(i,j)
        
        
print("========== Break Looping ===========")    
"""
Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis
keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.
Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan 
sesuai dengan tingkatan atau letak perulangannya berada.
"""
for i in range(2):       # Perulangan tingkat pertama
    print("Outer loop : ", i)
    for j in range(10):   # Perulangan tingkat kedua
        print("Inner loop : ", j)
        if j == 1:
            break   # Menghentikan perulangan dalam jika j = 1
        
# contoh lain break
for huruf in "Din ar":
    if huruf == " ":    # program akan berhenti jika bertemu huruf " " (spasi) yang berada pada teks "Din ar". 
        break
    print("Huruf saat ini : {}".format(huruf))  # <- {} yaitu untuk mengisi valuenya

# Continue
"""
Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya.
Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.
"""
print("========== Continue Looping ===========") 
for huruf in "Din ar":
    if huruf == " ":    # Program akan mengabaikan spasi dan akan dilanjutkan/ intinya apapun statement yang sama di continue dia akan diabaikan
        continue
    print("Huruf saat ini : {}".format(huruf))


print("========== Else setelah While ===========") 
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
"""
Pada contoh di atas, kita mencoba menampilkan angka dari 9 hingga 1. Program akan berhenti ketika angka 
tersebut adalah 7. Namun, lihat baik-baik bahwa else tidak tercetak di sini. Hal ini disebabkan while 
tersebut masih bernilai benar walaupun program keluar karena "break". 
"""

print("========== Pass ===========") 
"""
Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau
blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
"""
x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
    
    
print("========== List Comprehension ===========") 
# Masih terkait perulangan, terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.
angka = [1,2,3,4,5,6,7]
pangkat = []
for a in angka:
    pangkat.append(a**2)
print(pangkat)

# contoh lebih ringkasnya
angka2 = [1,2,3,4]
pangkat2 = [a**2 for a in angka2]
print(pangkat2)

# rumusnya 
"""
new_list = [expression for_loop_one_or_more_conditions]
"""