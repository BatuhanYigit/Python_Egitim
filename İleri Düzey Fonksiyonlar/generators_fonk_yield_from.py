def uretec1():
    yield "Üreteç 1 Çalıştı"
    yield "Üreteç 1 Durdu"

def uretec2():
    yield "Üreteç 2 Çalıştı"
    yield from uretec1()
    yield "Üreteç 2 Durdu"

for i in uretec2():
    print(i)