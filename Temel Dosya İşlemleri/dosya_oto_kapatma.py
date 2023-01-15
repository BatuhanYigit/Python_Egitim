try:
    dosya = open("/home/batuhan/Documents/GitHub/Python_Egitim/Temel Dosya İşlemleri/deneme.txt", "r")

except IOError:
    print("Bir hata oluştu")

finally:
    dosya.close()

# 2. otomatik kapatma yöntemi ise

with open("/home/batuhan/Documents/GitHub/Python_Egitim/Temel Dosya İşlemleri/deneme.txt", "r") as dosya1:
    print(dosya1.read())