# meminta input tahun dari user
tahun = int(input("Masukkan tahun: "))

# logika untuk menentukan tahun kabisat
if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print(tahun, "adalah tahun kabisat")
        else:
            print(tahun, "bukan tahun kabisat")
    else:
        print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")