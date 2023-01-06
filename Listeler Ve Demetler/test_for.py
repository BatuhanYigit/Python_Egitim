sayilar = [[0, 10], [6, 60], [12, 54], [67, 99]]

for i in sayilar:
    print(range(i[0],i[1]))

for i in sayilar:
    print(*range(*i))