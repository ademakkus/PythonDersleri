# Kullanıcı dışarıdan string olarak sayı dizi gönderecek :)

# 3 4 5 6 77.7 77 77 4 12.3 54 54.67 gibi
# gelen string değeri geriye sayısal bir dizi olarak döndürünüz.

def TryParse(sayi):
    try:
        int(sayi)
        return  True
    except:
        return False

# print(TryParse("12"))

def ConvertToList(string):
    myList = string.split()
    for n in range(len(myList)):
        if myList[n].count("."):
            myList[n] = float(myList[n])
        else:
            myList[n] = int(myList[n])
    return myList

result = ConvertToList("3 4 5 6 77.7 77 77 4 12.3 54 54.67")
print(result)

# [3.0, 4.0, 5.0, 6.0, 77.7, 77.0, 77.0, 4.0, 12.3, 54.0, 54.67]
# [3, 4, 5, 6, 77.7, 77, 77, 4, 12.3, 54, 54.67]