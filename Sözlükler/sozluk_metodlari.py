#Keys() Metodu
#eğer bir sözlüğün sadece anahtarlarını almak isterseniz keys() metodundan yararlanabilirsiniz:
sozluk_key = {"a":3,
"b":4,
"c":5,
}
print(sozluk_key.keys())
#dict_keys(['a', 'b', 'c'])

#Keys Metodu Dönüştürme İşlemleri

liste_key = list(sozluk_key.keys())
print("Liste Key : ",liste_key)
#['a', 'b', 'c']

tuple_key = tuple(sozluk_key.keys())
print("Tuple Key : ",tuple_key)
#('a', 'b', 'c')

karakter_dizesi = ",".join(sozluk_key.keys())
print("Karakter Dizesi : ",karakter_dizesi)
#a,b,c

#Values() Metodu
#keys() metodu bir sözlüğün anahtarlarını veriyor. Bir sözlüğün değerlerini ise values() metodu verir:

print("Values Metodu : ",sozluk_key.values())
#dict_values([3, 4, 5])

liste_values = list(sozluk_key.values())
print("Liste Values : ",liste_values)
#[3, 4, 5]

tuple_values = tuple(sozluk_key.values())
print("Tuple Values : ",tuple_values)
#(3, 4, 5)

karakter_dizesi_values = "".join([str(i) for i in sozluk_key.values()]) # value değeri int olduğu için string e çevirme işlemi yaptık

print("Values Karakter Dizesi",karakter_dizesi_values)
#345

#İtems() Metodu
#Bu metot, bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar:
#Bu metot sıklıkla for döngüleri ile birlikte kullanılarak bir sözlüğün anahtar ve değerlerinin manipüle edilebilmesini sağlar:

print("İtems Metodu :",sozluk_key.items())
#dict_items([('a', 3), ('b', 4), ('c', 5)])

# Örnek KUllanım : 

for anahtar,deger in sozluk_key.items():
    print("{} = {} ".format(anahtar,deger))
# a = 3 
# b = 4 
# c = 5

#Clear() Metodu

# Bu kelime İngilizce’de “temizlemek” anlamına gelir. Görevi sözlükteki öğeleri temizlemektir. 
# Yani içi dolu bir sözlüğü bu metot yardımıyla tamamen boşaltabiliriz:


lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu",
"üçüncü": "Adana Gençlerbirliği"}

print(lig)
#{'şampiyon': 'Adana Demirspor', 'ikinci': 'Mersin İdman Yurdu', 'üçüncü': 'Adana Gençlerbirliği'}

lig.clear()
print(lig)
#{}

#Copy() Metodu

hava_durumu = {"İstanbul": "yağmurlu", "Adana": "güneşli", "İzmir": "bulutlu"}
yedek_havadurumu = hava_durumu.copy()

print(hava_durumu)

hava_durumu["Hatay"] = "Güneşli"

print(hava_durumu)
print(yedek_havadurumu) # COpy metodu sayesinde havadurumuna eklediğimiz öğe yedek hava durumuna gelmedi


#fromkeys() Metodu

# fromkeys() metodu öteki metotlardan biraz farklıdır. Bu metot mevcut sözlük üzerinde işlem yapmaz. 
# fromkeys()’in görevi yeni bir sözlük oluşturmaktır.
#  Bu metot yeni bir sözlük oluştururken listeler veya demetlerden yararlanır

elemanlar = "Batuhan", "Ahmet", "Recep","Mert","Buray"

adresler = dict.fromkeys(elemanlar, "Kadıköy")

print(adresler)

#{'Batuhan': 'Kadıköy', 'Ahmet': 'Kadıköy', 'Recep': 'Kadıköy', 'Mert': 'Kadıköy', 'Buray': 'Kadıköy'}

#setdefault() Metodu

sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}

sepet.setdefault("içecekler", ("su","kola"))

print(sepet)
#{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola')}

print(sepet.setdefault("meyveler",("erik","çilek")))
#('elma', 'armut')

# Gördüğünüz gibi, sözlükte zaten “meyveler” adlı bir anahtar bulunduğu için, Python aynı adı taşıyan ama değerleri farklı olan yeni bir “meyveler” anahtarı oluşturmadı.
#  Demek ki bu metot yardımıyla bir sözlük içinde arama yapabiliyor, 
# eğer aradığımız anahtar sözlükte yoksa, setdefault() metodu içinde belirttiğimiz özellikleri taşıyan yeni bir anahtar-değer çifti oluşturabiliyoruz.

#Update() Metodu

stok = {"Elma":5,"armut":10,"peynir":6,"sosis":15}

yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

print(stok)
#{'Elma': 5, 'armut': 10, 'peynir': 6, 'sosis': 15}

stok.update(yeni_stok)

print(stok)
#{'Elma': 5, 'armut': 20, 'peynir': 8, 'sosis': 4, 'elma': 3, 'sucuk': 6}

























