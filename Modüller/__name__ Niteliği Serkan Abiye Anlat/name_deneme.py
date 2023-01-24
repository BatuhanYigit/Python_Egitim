sozluk = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

def ara(sozcuk):
    hata = "{} Kelimesi Sözlükte Yok"
    print(sozluk.get(sozcuk, hata.format(sozcuk)))

def ekle(sozcuk, anlam):
    mesaj = "{} Kelimesi sözlüğe eklendi!"
    sozluk[sozcuk] = anlam
    print(mesaj.format(sozcuk))

def sil(sozcuk):
    try:
        sozluk.pop(sozcuk)
    except KeyError as err:
        print(err, "Kelimesi Bulunamadı")
    else:
        print("{} kelimesi sözlükten silindi!".format(sozcuk))


if __name__ == "__main__":
    print('1. Sözlükte kelime ara')
    print('2. Sözlüğe kelime ekle')
    print('3. Sözlükten kelime sil')
    no = input("Yapmak istediğiniz işlemi giriniz : ")

    if(no == "1"):
        sozcuk = input("Aramak istediğiniz sözcük : ")
    elif(no == "2"):
        sozcuk = input("Eklemek istediğiniz sözcük : ")
        anlam = input("Eklemek istediğiniz sözcüğün anlamı : ")
        ekle(sozcuk,anlam)
    elif(no == "3"):
        sozcuk = input("Sileceğiniz Sözcük: ")
        sil(sozcuk)
    else:
        print("Yanlış işlem")