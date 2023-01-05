sayilar = 0
notlar = []

for i in range(10):
    veri = int(input("{}. not: ".format(i+1)))
    sayilar += veri
    notlar += [veri]
print("Girdiğiniz notlar : ",*notlar)
print("NOt ortalamanız : ",sayilar/10)