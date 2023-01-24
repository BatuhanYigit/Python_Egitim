def ters_cevir(s):
    if len(s) <1:
        return s
    else:
        ters_cevir(s[1:])
        print(s[0])
        



ters_cevir("Batuhan")