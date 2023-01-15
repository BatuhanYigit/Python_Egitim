dosya = open("/home/batuhan/Documents/GitHub/Python_Egitim/Temel Dosya İşlemleri/deneme.txt","r")

print(dosya.read())

print("Seek KOmutu KUllanmadan ...")

print(dosya.read())

print("Seek Komutu kullanıp...")

dosya.seek(0)
print(dosya.read())
print(dosya.tell())

print("Seek komutuna değer girip ..")

dosya.seek(10)
print(dosya.read())

#Seek kullanarak istediğimiz bayt kısmına gidebiliyoruz.