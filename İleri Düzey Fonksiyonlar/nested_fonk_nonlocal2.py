def yazici(mesaj):
    def yaz():
        nonlocal mesaj
        mesaj += " Dünya"
        print(mesaj)
    return yaz

y = yazici("Merhaba")

print(y())