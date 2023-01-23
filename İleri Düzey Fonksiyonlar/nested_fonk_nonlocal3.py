def sayici():
    sayi = 0
    print("Deneme")
    def say():
        nonlocal sayi
        sayi += 1
        return sayi
    return say

fonksiyon = sayici()

print(sayici())


print(fonksiyon())
print(fonksiyon())
print(fonksiyon())
print(fonksiyon())