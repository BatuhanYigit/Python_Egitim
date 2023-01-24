sozluk = {
    "Kitap":    "Book",
    "Bilgisayar": "Computer",
    "Programlama":"Programming"}

def ara(sozcuk):
    hata = "{} Kelimesi Sözlükte yok"
    return sozluk.get(sozcuk, hata.format(sozcuk))