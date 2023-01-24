import sys

sys.path.append(r'/home/batuhan/Documents/GitHub/Python_Egitim/Modüller/Modül Oluşturma/sozluk.py')



sozluk = {
    "Kitap":    "Book",
    "Bilgisayar": "Computer",
    "Programlama":"Programming"}

def ara(sozcuk):
    hata = "{} Kelimesi Sözlükte yok"
    return sozluk.get(sozcuk, hata.format(sozcuk))

def ekle(sozcuk, anlam):
    print("Anlam :",anlam)
    print("Sözcük : ",sozcuk)
    mesaj = "{} kelimesi sözlüğe eklendi "
    
    sozluk[sozcuk] = anlam

    print(mesaj.format(sozcuk))

def sil(sozcuk):
    try:
        sozluk.pop(sozcuk)
    except KeyError as err:
        print(err, "Kelimesi Bulunamadı")
    else:
        print("{} Kelimesi SÖzlükten silindi".format(sozcuk))