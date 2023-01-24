def yaz(sayi):
    for i in range(sayi):
        print("Merhaba Batuhan")
        yield

y = yaz(4)
for i in y:
    print(i)