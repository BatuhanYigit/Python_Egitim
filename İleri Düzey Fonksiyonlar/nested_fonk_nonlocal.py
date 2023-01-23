def kapsayici_fonk():
    non_local_degisken = 1
    def ic_fonk():
        nonlocal non_local_degisken
        non_local_degisken += 1
        print(non_local_degisken)
    return ic_fonk

donus_fonk = kapsayici_fonk()

print(donus_fonk())