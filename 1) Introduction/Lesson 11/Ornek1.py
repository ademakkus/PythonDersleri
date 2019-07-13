# dışarıdan girilen, metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını bulunuz :)

# print(chr(65))  # A
# print(ord("A")) # 65


def MetinToplamDeger(string):
    string = string.replace(" ","")
    havuz = 0
    liste = list(string)
    for i in liste:
        havuz += ord(i)
    return havuz

metin = input("Lütfen metin girin hoca söyledi : ")

result = MetinToplamDeger(metin)
print(result)
