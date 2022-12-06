#Diyelim ki kullanıcıya olası bir hata durumunda hem kendi yazdığınız hata mesajını, 
# hem de özgün hata mesajını göstermek istiyorsunuz.
# İşte Aşağıda ki yapı böyle durumlarda işe yarayabilir:

ilk_sayi = input("İlk Sayıyı Giriniz : ")
ikinci_sayi = input("İkinci Sayıyı Giriniz : ")

try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=",sayi1/sayi2)
except ValueError as hata:
    print("Sadece Sayı Giriniz !!!")
    print("Orjinal Hata  = ",hata)