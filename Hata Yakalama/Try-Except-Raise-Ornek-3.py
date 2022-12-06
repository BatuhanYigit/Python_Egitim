try:
    bolunen = int(input("İlk Sayıyı Giriniz :  "))
    bolen = int(input("İkinci Sayıyı Giriniz :  "))
    print(bolunen/bolen)
except(ZeroDivisionError):
    print("Bir Sayıyı 0 A bölemezsiniz !!! ")
    raise
