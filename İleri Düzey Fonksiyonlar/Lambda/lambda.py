cift_mi = lambda sayi: sayi % 2 == 0

print(cift_mi(100))

topla = lambda sayi1, sayi2: sayi1+sayi2

print(topla(100,100))

birlestir = lambda ifade, birlestirici: birlestirici.join(ifade.split())

print(birlestir("Birsen Karakütük Marmara Üniversitesi","-"))