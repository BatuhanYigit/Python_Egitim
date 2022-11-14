#Ama eğer istersek print() fonksiyonunun, çıktılarını ekrana değil, bir dosyaya yazdırmasını da sağlayabiliriz. 
# Mesela biz şimdi print() fonksiyonunun deneme.txt adlı bir dosyaya çıktı vermesini sağlayalım.
dosya = open("deneme.txt", "w")
print("Ben", "Batuhan", "Yigit", file=dosya)
dosya.close()

#Gelin isterseniz bununla ilgili bir örnek daha yapalım.
#  Mesela kişisel bilgilerimizi bir dosyaya kaydedelim.
#  Öncelikle bilgileri kaydedeceğimiz dosyayı oluşturalım

f = open("batuhanygt.txt", "w")

print("Batuhan yigit", file=f)
print("Funda Ergin", file=f)
print("Ahmet Ucarkus", file=f)
print("Fatma Kara", file=f)

f.close()

