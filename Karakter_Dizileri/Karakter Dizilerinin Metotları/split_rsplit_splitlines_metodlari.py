batuhan = "Batuhan Can Yiğit"

print(batuhan.split())

for i in batuhan.split():
    print(i)

kisaltma = input("Kıslatmasını öğrenmek istediğiniz kurum adını giriniz : ")

for i in kisaltma.split():
    print(i[0], end="")

deneme = "İstanbul, Lüleburgaz, Laleli, Hataylı,"
print(deneme)

for i in deneme:
    print(i)

for i in deneme.split("l"):
    print(i)

split_deneme = "Ankara Büyükşehir Belediyesi"

print(split_deneme.split(" "))

#>> ['Ankara', 'Büyükşehir', 'Belediyesi']

print(split_deneme.split(" ", 1)) #  1 sayısı sayesinde bölme işlemi karakter dizisi üzerine bir kez uygulandı. 

#>> ['Ankara', 'Büyükşehir Belediyesi']

print(split_deneme.rsplit(" ",1)) # Sağdan sola doğru bölme işlemi yapıyor.
#>> ['Ankara Büyükşehir', 'Belediyesi']

metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

print(metin.splitlines()) # splitlines satırlara ayırma işlemi yapar.
print(metin.splitlines(True)) # ayırdığı yerleri /n ile gösterir.




