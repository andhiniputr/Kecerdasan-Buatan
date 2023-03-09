print("ENTRY DATA BONUS PENJUALAN TOKO")
print("=========================")
jb = int(input("Masukkan Jumlah Barang : "))
harga = int(input("Masukkan Total Pembelian : "))
print("Bonus yang Didapat : ")
if jb > 5 and harga >= 500000:
    print("Selamat Anda Mendapatkan Bonus 1 Buah Setrika")
elif jb > 3 and harga >= 100000:
    print("Selamat Anda Mendapatkan Bonus 1 Buah Payung")
elif jb > 2 and harga >= 50000:
    print("Selamat Anda Mendapatkan Bonus 1 Buah Pena")
else:
    print("Maaf Anda Belum Mendapatkan Bonus")
