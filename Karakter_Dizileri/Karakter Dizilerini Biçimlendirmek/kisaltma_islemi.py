isim = input("İsminizi Gİriniz : ")

if len(isim)<= 5:
    print(isim[:5])
else:
    print(isim[:5]+"...")

isim1 = "Mertcan"
isim2 = "Batuhan"



print("MERHABA %s Merhaba %s" %(isim1,isim2))

print("ELMANIN FİYATI %(elma)s armutun fiyatı %(armut)s " %{"elma": 25,"armut":35})

print("NAİM {}".format("selam"))

print(f"hello {isim2}")
