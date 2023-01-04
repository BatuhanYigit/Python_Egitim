veri = input("Mesajınız : ")
bol = veri.split()

for i in bol:
    if i.isupper():
        print("Tamamı BÜyük harflerden oluşan kelimeler kullanmayınız.")
   