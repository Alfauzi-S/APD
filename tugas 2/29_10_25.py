# Tugas APD deadline minggu depan (5/11/2025)
# 1. Menjumlahkan data dalam list
# 2. Mencari nilai maksimum dalam list 
# Gunakan rekursif

data = [1,4]

def jumlah(data):
    if not data:
        return 0
    else:
        return data[0] + jumlah(data[1:]) # hasil pemanggilan fungsi jumlah() pada sisa list (slice list mulai dari indeks 1).
        
print(jumlah(data))

def maksimum(data):
    if len(data) == 1:
        return data[0]
    else:
        a = maksimum(data[1:]) # Cari nilai maksimum dari sisa list
        # Bandingkan elemen pertama dengan nilai maksimum dari sisa list
        # return max(data[0], a)
        if data[0] > a:
            return data[0]
        else:
            return a

print(maksimum(data))

def minimum(data):
    if len(data) == 1:
        return data[0]
    else:
        a = minimum(data[1:])
        # return min(data[0], a)
        if data[0] < a:
            return data[0]
        else:
            return a
        
print(minimum(data))