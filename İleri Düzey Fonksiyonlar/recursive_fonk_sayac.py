def sayac(sayi,sinir):
    print(sayi)
    if sayi == sinir:
        return "Bitti"

    else:
        return sayac(sayi+1,sinir)

print(sayac(5,30))