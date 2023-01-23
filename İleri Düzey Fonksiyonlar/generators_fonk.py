def fonksiyon_sayici():
    sayi = 0
    def say():
        nonlocal sayi
        sayi += 1
        return sayi
    return say

def uretec_sayici():
    sayi = 0
    while True:
        sayi += 1
        yield sayi

print(type(fonksiyon_sayici))
#<class 'function'>
print(type(uretec_sayici))
#<class 'function'>

fonksiyon = fonksiyon_sayici()
print(type(fonksiyon))
#<class 'function'>
uretec = uretec_sayici()
print(type(uretec))
#<class 'generator'>