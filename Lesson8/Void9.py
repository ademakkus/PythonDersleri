# Dışarıdan aldığı değere göre kare çizen metot

def kare_ciz(sayi):
    index = 0
    while index <= sayi:
        metin = ""
        for i in range(sayi):
            metin += "X  "
        print(metin)
        index += 1

kare_ciz(10)

# -----------------------

def kare_ciz_(sayi):
    index = 0
    while index <= sayi:
        print("X  "* sayi)
        index += 1

kare_ciz_(10)

# -----------------------

def kare_ciz__(sayi):
    for i in range(sayi + 1):
        print("X  " * sayi)

kare_ciz__(10)