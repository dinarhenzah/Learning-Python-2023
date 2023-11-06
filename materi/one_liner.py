"""
One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode 
hanya dalam satu baris. One-liner adalah salah satu keunggulan dalam Python yang susah untuk 
diimplementasikan bagi beberapa bahasa pemrograman lainnya.

Tujuan dari one-liner ini adalah membuat satu baris kode yang singkat dan jelas. Perlu diingat bahwa 
tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas. 
"""

# kalo mau run salah satu cara bisa di komentar dulu

# variable
x = 1
y = 2

# Cara 1
temp = x
x = y
y = temp

# Cara 2
x, y = y, x    # One-liner

# Output
print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

