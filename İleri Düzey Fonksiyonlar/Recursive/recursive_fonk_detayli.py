def sirala(s):
    if len(s) <1:
        return s
    else:
        print("Öz yineleme sürecine girerken : ",s)
        sirala(s[1:])
        print("Öz yineleme sürecinden çıkarken : ",s)


sirala("Batuhan Yiğit")