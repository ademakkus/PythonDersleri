# map metodu, ilk parametrede sizden bir metot ister, 2. parametrede ise o metodun alacağı veri tipine uygun bir değeri ister, map metodu 2. parametrede verilen her bir değer için 1. parametredeki metodu çalıştırıp sonucu size teslim edecektir

def square(num):
    return  num**2


my_nums = [1,2,3,4]


for item in map(square,my_nums):
    print(item)



liste = list(map(square,my_nums))
print(liste)