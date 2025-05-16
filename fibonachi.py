def fibonachi (n):
    if n <= 0:
        print("Fibonachi tidak ketemu!")
    elif n == 1 or n  == 2:
        return 1
    else:
        return (fibonachi(n - 1)) + (fibonachi (n - 2))
    
a = int(input("Masukkan angka: "))
cari_fibonachi = fibonachi(a)
print("Nilai fibonachinya adalah:", cari_fibonachi)
