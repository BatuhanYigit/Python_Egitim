with open("/home/batuhan/Documents/GitHub/Python_Egitim/Temel Dosya İşlemleri/deneme.txt","r+") as dosya:
    veri = dosya.read()
    dosya.seek(0) # dosyanın en başına gidiyoruz.
    dosya.write("Bu bir deneme başlangıç\n"+veri)
