ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for i in ilk_metin: #ilk_metin'deki, 'i' adını verdiğimiz bütün öğeler için
    if not i in ikinci_metin: #eğer 'i' adlı bu öğe ikinci_metin'de yoksa
        print(i) #'i' adlı öğeyi ekrana bas
