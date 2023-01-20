#Pop() Metodu

sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"),
"içecekler": ("su", "kola", "ayran")}

sorgu = input("Silmek istediğiniz öğeyi yazınız meyveler,sebzeler,içecekler : ")

sepet.pop(sorgu, "Bölye bir şey yok bunu silemezsiniz!")
print(sepet)