sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = "Batuhan"

for i in kelime:
    if i in sesli_harfler:
        sesliler += i
    else:
        sessizler += i
    
print("Sesli Harfler = ",sesliler)
print("Sessiz Harfler = ",sessizler)