

veri = input("KÜçük Harflerle isminizi giriniz : ")

if not veri.islower():
    print("İsminizin tamamını küçük harf kullanın!")

else:
    print("Hoşgeldin {}".format(veri))