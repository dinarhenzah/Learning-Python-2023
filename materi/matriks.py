import numpy
import sys

matriks = numpy.array([[1, False, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

# Perbandingan ukuran menggunakan matriks Python dan matriks NumPy
var_list = [[1, 2, 3]]
var_array = numpy.array([[1, 2, 3]])
            
print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
print("=========Deklarasi Nilai Default==========")

# DEKLARASI NILAI DEFAULT
# eksample -> nama-var = [[<default-var> for j in range(m)] for i in range(n)]
# default-var = bebas kesepakatan bersama misal 1-10
# n = baris, m = kolom
matriks1 = numpy.array([[0 for j in range(3)] for i in range(4)])
print(matriks1)
"""
Pada kode di atas, kita mendeklarasikan variabel matriks dan menginisialisasikannya dengan nested list 
dan nested for serta nilai default-nya adalah 0. Matriks yang dibuat pada program di atas adalah 
matriks value dengan setiap elemennya bertipe integer serta memiliki ukuran baris = 3 dan ukuran kolom = 4.
"""
print("=========Akses Elemen Matriks=========")

# AKSES ELEMEN MATRIKS
var_mat = numpy.array([[1, 2, 3, 4, 5], # baris 0
           [6, 7, 8, 9, 10],            # baris 1
           [11, 12, 13, 14, 15],        # baris 2
           [16, 17, 18, 19, 20],        # baris 3
           [21, 22, 23, 24, 25]])       # baris 4

print(var_mat[3][1]) # baris dulu baru kolom
print("=========Operasi Matriks 2x2=========")

# OPERASI MATRIKS 2X2
var_mat = numpy.array([[5, 0],
                       [1, -2]])
def_mat = numpy.array([[0 for j in range(2)] for i in range(2)])

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2 # <- nilai 2 tersebut sebagai kostanta dan dia akan dikalikan dengan nilai yang terdapat di var_mat 
print(def_mat)

print("=========Operasi Matriks 2x2 Efektif=========")

# OPERASI MATRIKS 2X2 (Cara yang lebih efektif menggunakan numpy)
var_mat1 = numpy.array([[5, 0],
                       [1, -2]])
result = var_mat1 * 2
print(result)