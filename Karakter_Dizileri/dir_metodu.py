print(dir(int))

for i in dir(int):
    if "_" not in i[0]:
        print(i)