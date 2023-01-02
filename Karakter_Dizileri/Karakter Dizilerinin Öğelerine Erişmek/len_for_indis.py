nesne = "Batuhan"

len(nesne)

print(len(nesne))

#>> 7 değerini elde ettik fakat indisler 0 dan başlar bu yüzden bu değer bizim için YANLIŞ

print(nesne[len(nesne)-1])

#>> bu şekilde dizide ki son karakteri elde ettik yani N harfini bu komut bize dizide kaç indis olduğunu doğru bir şekilde veriyor.

#>> Hadi FOR döngüsü ile karakterleri bastıralım 

for karakter in range(len(nesne)):
    print(nesne[karakter])

#>> Burada range fonksiyonu yukarıda ki tanımlamayı kendi yaptı.

#>> Hadi for döngüsüyle bir örnek yapalım
isim = input("İsminizi Giriniz : ")
for i in range(len(isim)):
    print("İsminizin {}. harfi : {} ".format(i+1, isim[i]))

#>> Fakat ilk karakterimiz 0 diyor bu yanıltıcı olacağından i+1 fonksiyonunu ekledim.
