# Mengambil input jumlah bilangan dalam deret Fibonacci
n = int(input("Masukkan jumlah bilangan dalam deret Fibonacci: "))

# Inisialisasi bilangan pertama dan kedua
a, b = 0, 1

# Loop untuk menghasilkan deret Fibonacci
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
