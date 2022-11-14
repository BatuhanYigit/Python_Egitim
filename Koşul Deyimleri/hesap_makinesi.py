giris = """
****************** HESAP MAKİNESİ ******************
(1) Topla
(2) Çıkart
(3) Çarp
(4) Böl
(5) Karesini Hesapla
(6) Karekök Hesapla
"""

print(giris)

soru = input("Yapmak istediğiniz işlemi giriniz : ")

if(soru == 1):
    print("""
    ******************** Toplama İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    sayi2 = input("Bir sayı daha giriniz :  ")
    toplam = sayi1 + sayi2
    print("Sonuç = {}".format(toplam))
elif(soru == 2):
    print("""
    ******************** Çıkarma İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    sayi2 = input("Bir sayı daha giriniz :  ")
    toplam = sayi1 - sayi2
    print("Sonuç = {}".format(toplam))
elif(soru == 3):
    print("""
    ******************** Çarpma İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    sayi2 = input("Bir sayı daha giriniz :  ")
    toplam = sayi1 * sayi2
    print("Sonuç = {}".format(toplam))
elif(soru == 4):
    print("""
    ******************** Bölme İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    sayi2 = input("Bir sayı daha giriniz :  ")
    toplam = sayi1 / sayi2
    print("Sonuç = {}".format(toplam))
elif(soru == 5):
    print("""
    ******************** Kare Hesaplama İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    toplam = sayi1 ** 2
    print("Sonuç = {}".format(toplam))
elif(soru == 6):
    print("""
    ******************** Çıkarma İşlemi ********************
    """)
    sayi1 = input("Bir Sayı Giriniz :  ")
    toplam = sayi1 ** 0.5
    print("Sonuç = {}".format(toplam))
else:
    print("Yanlış işlem girdiniz")
