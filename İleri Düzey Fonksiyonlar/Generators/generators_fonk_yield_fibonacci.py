def fibonacci():
    x = 1
    y = 0
    z = 0
    while True:
        z = y
        y = x
        x = y+z
        yield x
"""
Fibonacci dizisi, 0 ve 1 ile başlayan ve her sayının kendisinden önce gelen iki sayının toplanması ile elde edildiği bir sayı dizisidir. İtalyan matematikçi Leonardo Fibonacci’den adını alır. 0, 1, 1 (0+1), 2 (1+1), 3 (1+2), 5 (2+3), 8 (3+5), 13 (5+8), 21 (8+13), 34 (13+21) şeklinde devam eder.

"""