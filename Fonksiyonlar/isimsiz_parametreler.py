def carp(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    print(sonuc)

carp(2,3,4,5)