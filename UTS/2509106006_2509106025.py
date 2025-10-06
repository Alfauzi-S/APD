
# Bab 1: Jalan Buntu Pertama dan Logika Logam

print('='*100)
ransum_tersedia = 7
tingkat_bahan_bakar = 0.45
nama_area = "Jurang Lupa"
cincin_aktif = True
print("Status Persediaan Elara:")
print("Ransum (Integer):", ransum_tersedia)
print("Bahan Bakar Obor (Float):", tingkat_bahan_bakar)
print("Lokasi (String):", nama_area)
print("Cincin Hangat Aktif (Boolean):", cincin_aktif)

# Bab 2: Keputusan di Jembatan Patahan

print('='*100)
tingkat_bahan_bakar = float(input("tingkat bahan bakar :"))
ransum_tersedia = int(input("masukan ransum tersedia :"))

if tingkat_bahan_bakar > 0.3 and ransum_tersedia < 5:
    print("Keputusan: Lompat. Risiko dapat diambil karena persediaan tipis.")
elif tingkat_bahan_bakar > 0.3:
    print("Keputusan: Tidak perlu lompat. Energi obor cukup, cari jalan memutar yang aman.")
else:
    print("Keputusan: Waspada. Persediaan bahan bakar rendah, prioritaskan keselamatan.")

# Bab 3: Ujian Kebugaran dengan Perulangan

print('='*100)
batas_pendakian = 25
jumlah_langkah_saat_ini = 0

print("Elara memulai pendakian...")

while jumlah_langkah_saat_ini < batas_pendakian:
    jumlah_langkah_saat_ini += 1
    print(f"Langkah ke: {jumlah_langkah_saat_ini}")
    if jumlah_langkah_saat_ini % 5 == 0:
        print(f"(Menarik napas sejenak. Ini adalah langkah ke-{jumlah_langkah_saat_ini})")
print(f"Istirahat. Batas pendakian {batas_pendakian} langkah tercapai. Puncak sudah dekat.")

# Bab 4: Menghitung Persediaan dengan Perulangan Terbatas

print('='*100)
daftar_barang = ["Obor Abadi", "Ransum", "Peta Usang", "Kompas Logika", "Jubah Pelindung"]
nilai_per_barang = [20, 5, 10, 15, 30]
total_nilai = 0

print("Elara mengecek nilai persediaan:")

for i in range(len(daftar_barang)):
    nilai_barang_saat_ini = nilai_per_barang[i]
    total_nilai += nilai_barang_saat_ini
    print(f"{daftar_barang[i]} memiliki nilai: {nilai_barang_saat_ini}")

print(f"\nTotal Nilai Semua Barang: {total_nilai} Koin Emas.")

# Bab 5: Pengaturan Inventaris yang Fleksibel

print('='*100)
inventaris_elara = ["Peta Usang", "Kompas Logika", "Ransum Biasa", "Ransum Biasa", "Ransum Biasa"]

print("Inventaris Awal:", inventaris_elara)
print("Jumlah item awal:", len(inventaris_elara))

inventaris_elara.append("Kayu Sihir")
inventaris_elara.append("Batu Memori")

print("\nSetelah Menemukan Item Baru:", inventaris_elara)

inventaris_elara.remove("Ransum Biasa")
inventaris_elara.remove("Ransum Biasa")
inventaris_elara.remove("Ransum Biasa")
inventaris_elara.append("Ransum Konsentrat")

print("\nSetelah Melakukan Penukaran Ransum:", inventaris_elara)
print("Jumlah total item akhir (len):", len(inventaris_elara))

# Bab 6: Koordinat Gerbang yang Tak Tergantikan

print('='*100)
koordinat_gerbang = (45.78, 120.33, 'North_Wing')
kode_aktivasi = ('Alpha', 7, 'Kuno')

print("Koordinat Gerbang (Data Tetap):", koordinat_gerbang)
print("Kode Aktivasi (Data Tetap):", kode_aktivasi)

kunci_gerbang_lengkap = koordinat_gerbang + kode_aktivasi

print("Kunci Gerbang Lengkap (Hasil Gabungan):", kunci_gerbang_lengkap)

# Bab 7: Analisis Rune Unik

print('='*100)
koleksi_rune_mentah = ["Rune Angin", "Rune Tanah", "Rune Angin", "Rune Air", "Rune Api", "Rune Api", "Rune Tanah", "Rune Cahaya"]

print("Koleksi Rune Mentah (dengan Duplikasi):", koleksi_rune_mentah)

koleksi_rune_unik = set(koleksi_rune_mentah)
print("\nRune Unik yang Ditemukan (Menggunakan Set):", koleksi_rune_unik)

daftar_rune_terurut = list(koleksi_rune_unik)

daftar_rune_terurut.sort()
print("\nDaftar Rune Unik yang Telah Diurutkan (.sort()):", daftar_rune_terurut)

# Bab 8: Perhitungan Strategi Perbekalan

print('='*100)
persediaan_porsi = [2.0, 2.0, 2.0, 2.0, 1.0]
konsumsi_harian = 1.5
hari_bertahan = 0
total_porsi = 0.0

for porsi in persediaan_porsi:
    total_porsi += porsi

print(f"Total Porsi Tersedia: {total_porsi}")
print(f"Konsumsi Harian: {konsumsi_harian} porsi\n" + "-"*20)

while total_porsi >= konsumsi_harian:
    hari_bertahan += 1
    total_porsi -= konsumsi_harian
    
    print(f"Hari ke-{hari_bertahan}: Konsumsi {konsumsi_harian} porsi.")
    if hari_bertahan % 2 != 0:
        total_porsi -= 0.2
        print(f"  -> Kelelahan (Hari Ganjil), konsumsi ekstra 0.2 porsi. Sisa: {total_porsi:.1f}")
    else:
        print(f"  -> Sisa porsi: {total_porsi:.1f}")

print("-" * 20 + f"\nSIMULASI SELESAI. Elara dapat bertahan selama: {hari_bertahan} hari penuh.")

# Bab 9: Pembentukan Tim dan Evaluasi Moral

print('='*100)
daftar_anggota_mentah = ["Garen", "Lyra", "Zio", "Garen"]
nilai_moral = [8, 9, 7]
total_moral = 0

anggota_tim_unik = set(daftar_anggota_mentah)
jumlah_anggota = len(anggota_tim_unik)
anggota_list_terurut = sorted(list(anggota_tim_unik))

print("Anggota Tim Unik Terurut:", anggota_list_terurut)
print("Nilai Moral (Garen, Lyra, Zio):", nilai_moral)
print("-" * 25)

for moral in nilai_moral:
    total_moral += moral
rata_rata_moral = total_moral / jumlah_anggota

print(f"Total Poin Moral: {total_moral}")
print(f"Rata-rata Moral Tim: {rata_rata_moral}")


print("\n--- Evaluasi Moral Individu ---")
for i in range(jumlah_anggota):
    nama_anggota = anggota_list_terurut[i]
    moral_individu = nilai_moral[i]

    if moral_individu < rata_rata_moral:
        print(f"Peringatan: {nama_anggota} (Moral {moral_individu}) berada di bawah rata-rata. Beri motivasi!")
    else:
        print(f"Status: {nama_anggota} (Moral {moral_individu}) berada di atas atau sama dengan rata-rata. Bagus!")