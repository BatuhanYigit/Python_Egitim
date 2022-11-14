import os
d1 = open("/Users/batuhan.yigit/Desktop/Eğitim dosyaları/Python_Egitim/Döngüler/For/isimler1.txt", encoding="utf-8")
d1_satirlar = d1.readlines()

d2 = open("/Users/batuhan.yigit/Desktop/Eğitim dosyaları/Python_Egitim/Döngüler/For/isimler2.txt", encoding="utf-8")
d2_satirlar = d2.readlines()

for i in d2_satirlar:
    if not i in d1_satirlar:
        print(i)

d1.close()
d2.close()