# strip metodu

veri = "                    batuhan Yiğit                 "

print(veri)

#                     batuhan Yiğit                 

print(veri.strip())

#>batuhan Yiğit

il = "adana"

print(il)

#>adana

print(il.strip("a"))

#>dan

metin = """
> Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
> 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
> olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
> Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
> Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
> grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
> Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
> bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
"""

for i in metin.split():
    print(i.strip(">"), end=" ")
# Bu komut ile paragrafların başında ki > karakterini kaldırdık.

#rstrip ve lstrip

print(il.lstrip("a")) # verinin solunu temizler
#> dana

print(il.rstrip("a")) # Verinin Sağını temizler

#> adan