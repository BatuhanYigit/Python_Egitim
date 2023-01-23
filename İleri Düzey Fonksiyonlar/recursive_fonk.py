def sirala(s):
    if len(s) < 1:
        return s
    else:
        print(s)
        return sirala(s[1:])


print(sirala("batuhan"))