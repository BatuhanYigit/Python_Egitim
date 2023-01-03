
araba = "porsche"

print(araba)

print("P"+araba[1:])

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for i in site1,site2,site3,site4:
    print("http://", i, sep="")

#Eğer www. kısımlarını atmak isterseniz.
# Karakter dizisi birleştirme işlemleri ile birlikte dilimleme yöntemini de kullanmanız gerekir:

for i in site1,site2,site3,site4:
    print("http://",i[4:], sep="")

deneme = "batuhan"

deneme = deneme[:3] + "UH" + deneme[5:]

print(deneme)

# Çıktı >>> batUHan