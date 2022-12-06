#Bu blok içinde gerçekleşen hataları da daha sonra tek tek except... blokları yardımıyla yakalıyoruz.
#Ama eğer biz istersek bu kodlarda verilebilecek hataları gruplamayı da tercih edebiliriz:

try:
    bolen = int(input("İlk Sayıyı Giriniz : "))
    bolunen = int(input("İkinci Sayıyı Giriniz : "))
except ValueError:
    print("Lütfen Sadece Sayı Giriniz!!!!")
else:
    try:
        print(bolen/bolunen)
    except ZeroDivisionError:
        print("Bir Sayıyı 0 a bölemezsiniz !!")