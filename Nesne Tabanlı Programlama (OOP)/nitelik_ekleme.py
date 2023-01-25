class Calisan:
    kabiliyetleri = []
    unvanı = 'işçi'
    maaşı = 1500
    memleketi = ''
    doğum_tarihi = ''


ahmet = Calisan()
batuhan = Calisan()
recep = Calisan()
naim = Calisan()


ahmet.kabiliyetleri.append("Deneme")

print("Ahmetin Kabileyetleri : ",ahmet.kabiliyetleri)

hamza = Calisan()

print("Hamzanın Kabiliyetleri : ",hamza.kabiliyetleri)
# GÖrdüğünüz gibi deneme kabileyetini hamzayada eklemiş



"""
Hatırlarsanız, sınıf niteliklerinden bahsederken, bu niteliklerin önemli bir özelliğinin, sınıf çağrılmadan çalışmaya başlamaları olduğunu söylemiştik. Sınıf niteliklerinin bir başka önemli özelliği de, bu niteliklere atanan değerlerin ve eğer yapılabiliyorsa bu değerler üzerinde sonradan yapılan değişikliklerin o sınıfın bütün örneklerini etkiliyor olmasıdır. Eğer ilgili sınıf niteliği; karakter dizisi, demet ve sayı gibi değiştirilemeyen (immutable) bir veri tipi ise bu sınıf niteliği üzerinde zaten değişiklik yapamazsınız. Yaptığınız şey ancak ilgili sınıf niteliğini yeniden tanımlamak olacaktır. Ancak eğer sınıf niteliği, liste, sözlük ve küme gibi değiştirilebilir (mutable) bir veri tipi ise bu nitelik üzerinde yapacağınız değişiklikler bütün sınıf örneklerine yansıyacaktır


"""