liste = []

while True:
    sayi = input("Bir sayı giriniz : (Çıkmak için q) ")

    if sayi == "q":
        print(liste)
        break

    sayi = int(sayi)

    if sayi not in liste:
        liste += [sayi]
        print(liste)
    else:
        print("Bu sayıyı girdiniz!!")