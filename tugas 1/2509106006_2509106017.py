# Program Potongan Harga 20% untuk NIM dengan 3 Digit Akhir Bilangan Prima
# Dibuat oleh : 2509106006 - Muhammad Alfauzi Syahputra
#               2509106017 - Yoga Ananda Prasetya

ulang = "y" # variabel untuk mengulang program
while ulang == "y": # loop utama untuk mengulang program 
    print("=" * 80)
    print(r"Program Potongan Harga 20% untuk NIM dengan 3 Digit Akhir Bilangan Prima".center(80))
    print("=" * 80)

    # Input NIM
    NIM = int(input("Masukkan NIM (10 digit): "))

    # Hitung jumlah digit
    tesdigit = NIM # variabel sementara untuk menghitung digit
    digit = 0
    while tesdigit > 0:    # selama tesdigit lebih besar dari 0
        tesdigit //= 10    # floor division (hasil bagi dibulatkan ke bawah) dari tesdigit dibagi 10
        digit += 1

    print("-" * 80)
    print(f"{'Jumlah digit':22}: {digit}")

    # Cek apakah jumlah digit = 10
    if digit == 10:
        # Ambil 3 digit terakhir
        digitterakhir = NIM % 1000 # modulus (hasil bagi sisanya) dari NIM dibagi 1000 untuk mendapatkan 3 digit terakhir
        print(f"{'3 digit terakhir':22}: {digitterakhir}")

        # Hitung faktor untuk mengecek bilangan prima
        faktor = 0
        for i in range(1, digitterakhir + 1): # dari 1 sampai digitterakhir (start, stop, step)
            if digitterakhir % i == 0:
                faktor += 1
        print(f"{'Jumlah faktor':22}: {faktor}")

        # Cek bilangan prima
        if faktor == 2:
            print(f"{'Prima':22}: Iya")
            print("-" * 80)
            harga = float(input("Masukan harga         : "))
            diskon = harga * 0.20
            print(f"{'Diskon 20%':22}: {diskon:.2f}")
            total = harga - diskon
            print(f"{'Total':22}: {total:.2f}")
        else:
            print(f"{'Prima':22}: Tidak")
            print("-" * 80)
            print("Maaf, anda tidak mendapatkan potongan harga".center(80))
    else:
        print("NIM yang dimasukkan salah!")
    print("=" * 80)

    ulang = input("Apakah ingin mengulang program? (y/n): ")

print("=" * 80)
print("Program Selesai!".center(80))
print("=" * 80)