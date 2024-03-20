def interpolation_search(array, target):
    kiri = 0 #1
    kanan = len(array) - 1 #n #1'
    
    while kiri <= kanan and array[kiri] <= target <= array[kanan]: #log log n
        if kiri == kanan: 
            if array[kiri] == target:
                return kiri #n
            else:
                return -1 #1
        
        # Hitung posisi yang mungkin menggunakan interpolasi
        posisi = kiri + ((target - array[kiri]) * (kanan - kiri)) // (array[kanan] - array[kiri]) #n #6n'
        
        if array[posisi] == target:
            return posisi #n
        elif array[posisi] < target:
            kiri = posisi + 1 #1 #1'
        else:
            kanan = posisi - 1 #1 #1'
    
    return -1 #1

# Contoh penggunaan:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #1
target = 6 #1
hasil = interpolation_search(arr, target) #n
if hasil != -1:
    print(f"Elemen {target} ditemukan di indeks {hasil}") #1
else:
    print(f"Elemen {target} tidak ditemukan dalam array") #1
