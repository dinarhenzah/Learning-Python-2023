var_list = [1,2,3,4]

for elemen in var_list:
    print(id(elemen)) # perhatikan bahwa semua elemen tersebut memiliki ID lokasi penyimpanan yang berbeda.

# cara looping yg sama (0) -> bisa diganti    
var_arr = [0 for i in range(10)]
print (var_arr)

# cara looping berurutan
var_arr2 = [0 for i in range(10)]
for i in range(10):
    var_arr2[i] = i
print (var_arr2)

# cara mencari index
var_arr3 = [1,2,3,4,5,6,7,8,9]
print(var_arr3[2]) # <- dikasi kurung siku dibelakang

# PEMPROSESAN SKUENSIAL ARRAY
"""
1.Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
2.Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0. 
3.Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
4.Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
5.Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.
"""
# Contoh
var_skeu = [1,2,3,4,5]

for i in range(len(var_skeu)):
    current_element = var_skeu[i]
    next_index = i+1
    
    if next_index < len(var_skeu):
        next_element = var_skeu[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")
    
    
# Mencari nilai terbesar
var_angka = [1,454,7,2,89,3,123]
left_pointer = var_angka[0]

for i in range(1, len(var_angka)):
    right_pointer = var_angka[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)

