def LuasPersegiPanjang (panjang, lebar):
    return panjang*lebar

def KelilingPersegiPanjang (panjang, lebar):
    return 2*(panjang*lebar)

p = int(input("Masukkan nilai anjang persegi : "))
l = int(input("Masukkan nilai ebar persegi : "))
hasil_luas = LuasPersegiPanjang(p,l)
hasil_keliling = KelilingPersegiPanjang(p,l)
print("Luasnya adalah ", hasil_luas)
print("Kelilingnya adalah ", hasil_keliling)
