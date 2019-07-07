# Dışarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metot örneği

# C#  params

def Hesapla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return  toplam

result = Hesapla(1,2,3,4,5,6,7,8,9 ,10,11,12,13)
print(result)