isim = "batuhan"

print(isim)

#>> batuhan

print(isim.replace("b","B"))

#>> Batuhan

deneme = "kerem"

print(deneme)
#>> kerem

print(deneme.replace("e", ""))

#>> krm

veri = "memleket"

print(veri)

#>> memleket

print(veri.replace("e", "", 1)) # Burada 1 adet e harfinin silinmesini istedik

#>> mmleket

print(veri.replace("e","",2)) # Burada 2 adet e harfinin silinmesini istedik

#>> mmlket

print(veri.replace("e","",3)) # Burada 3 adet e harfinin silinmesini istedik

#>> mmlkt