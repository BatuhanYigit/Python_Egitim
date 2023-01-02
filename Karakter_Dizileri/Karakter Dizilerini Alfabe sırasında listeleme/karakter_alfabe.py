
alfabe = sorted("elma")

print(alfabe)

#>> Çıktımız bu şekilde ['a', 'e', 'l', 'm']

#Alışık olduğumuz şekilde print etmek istersek

print(*sorted("elma"), sep="") #>> Çıktımız "aelm" şeklinde olacak

#veya

for i in sorted("elma"):
    print(i, end="")