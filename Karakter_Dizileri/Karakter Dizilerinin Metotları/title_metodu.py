veri = "istanbul izmir imkan"
for kelime in veri.split():
    if kelime.startswith("i"):
        kelime = "İ" + veri[1:]
    kelime = kelime.title()

    print(kelime, end=" ")