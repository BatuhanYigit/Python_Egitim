def uretec():
    yield "Merhaba"
    yield "Batuhan"

generators = uretec()

print(next(generators))
#Merhaba

print(next(generators))
#Batuhan