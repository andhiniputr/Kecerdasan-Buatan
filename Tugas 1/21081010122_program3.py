print("JENIS - JENIS PERHITUNGAN")
print("1. Perhitungan Luas Lingkaran")
print("2. Perhitungan Keliling Belah Ketupat")
print("3. Perhitungan Volume Tabung")
perhitungan = int(input("Pilih Jenis Perhitungan : "))
if perhitungan == 1 :
    print("Rumus : phi * r * r")
    r = int(input("Nilai Jari - Jari :"))
    luas = 3.14 * r * r
    print("Luas lingkaran dengan jari - jari", r, " adalah : ", round(luas, 2))
elif perhitungan == 2 :
    print("Rumus : 4 * s")
    s = int(input("Nilai Sisi : "))
    kel = 4 * s
    print("Keliling belah ketupat dengan sisi", s, " adalah : ", round(kel, 2))
elif perhitungan == 3 :
    print("Rumus : phi * r * r * t")
    rsk = int(input("Nilai Rusuk : "))
    t = int(input("Nilai Tinggi : "))
    vol = 3.14 * rsk * rsk * t
    print("Volume tabung dengan rusuk", rsk, " dan tinggi", t, " adalah : ", round(vol, 2))
else :
    print("Anda salah memasukkan pilihan! Ulangi lagi!")
