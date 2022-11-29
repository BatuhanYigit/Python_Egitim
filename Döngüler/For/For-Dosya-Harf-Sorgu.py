d1 = open("/Users/batuhan.yigit/Desktop/Eğitim dosyaları/Python_Egitim/Döngüler/For/metin.txt", encoding="utf-8")
harf = input("Sorgulamak istediğiniz harf : ")
sayi = 0
for karakter_dizisi in d1:
    for karakter in karakter_dizisi:
        if harf in karakter:
            sayi+=1
print(sayi)
d1.close

#deneme