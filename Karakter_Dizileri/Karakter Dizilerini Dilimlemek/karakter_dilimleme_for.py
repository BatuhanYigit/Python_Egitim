site1 = "www.goturkiye.com"
site2 = "www.goistanbul.com"
site3 = "www.goankara.com"

for isim in site1,site2,site3:
    print("site : ",isim[4:-4])

#>>ilk 4 harften sonrası ve son 4 harften öncesi olarak komut girdik


ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca  kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

for ata in ata1,ata2,ata3,ata4,ata5:
    print(ata[0:-1])

#>> Bu örnekte ! işaretini ortadan kaldırdık haydi bu seferde sonlarına . işaretini koyalım

for ata in ata1,ata2,ata3,ata4,ata5:
    print(ata[0:-1]+".")


#>> Tersten Yazmak istediğimizde aşağıda ki şekilde işlem yapıyoruz.

kardiz = "Sana Gül Bahçesi Vadetmedim"

print(kardiz[::-1])

#>> İlk ve son indis belirtmedim çünkü tamamını alacaktım yani kısaca
#kardiz[ilk_karakter:son_karakter:atlama_sayısı]

#>>Dediğimiz gibi, yukarıdaki yöntemi kullanarak karakter dizilerini ters çevirebilirsiniz. 
#>>Ama eğer isterseniz reversed() adlı bir fonksiyondan da yararlanabiliriz.

for i in reversed("Sana Gül Bahçesi Vadetmedim"):
    print(i,end="")

#>> Veya
print(*reversed("Sana Gül Bahçesi Vadetmedim"), sep="")