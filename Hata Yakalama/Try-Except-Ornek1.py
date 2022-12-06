ilk_sayi = input("İlk Sayıyı giriniz : ")
ikinci_sayi = input("İkinci Sayıyı giriniz : ")
try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=", sayi1/sayi2)

except ValueError:
    print("Lütfen sadece sayı giriniz!!!!")
except ZeroDivisionError:
    print("Bir Sayıyı 0 A bölemezsiniz!!!")

# Bir farklı Kullanım şekili

# except (ZeroDivisionError,ValueError):