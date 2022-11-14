bolunen = int(input("Bir Sayı giriniz : "))
bolen = int(input("Bir Sayı Daha Giriniz : "))

mesaj = "{} Sayısı {} Sayısına tam".format(bolunen, bolen)

if(bolunen % bolen == 0):
    print(mesaj,"Bölünüyor")
else:
    print(mesaj, "Bölünmüyor")