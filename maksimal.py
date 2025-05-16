def max (angka1, angka2, angka3) :
    if ((angka1 > angka2) and (angka1 > angka3)) :
        return angka1
    elif ((angka2 > angka1) and (angka2 > angka3)) :
        return angka2
    else :
        return angka3
angka1= int(input("Masukan angka: "))
angka2= int(input("Masukan angka: "))
angka3= int(input("Masukan angka: "))

cek_max= max(angka1, angka2, angka3)
print ("Nilai maksimal dari ",angka1,",",angka2,",",angka3,"adalah ",cek_max)
