with open("/home/batuhan/Documents/GitHub/Python_Egitim/Temel Dosya İşlemleri/deneme.txt","r+") as dosya:
    veri = dosya.readlines()
    veri.insert(2,"2. SATIR BATUHAN\n")
    dosya.seek(0)
    dosya.writelines(veri)