# filter metodu, map metodu ile aynı mantıkla çalışır fakat, işlem sonucu True olan değerleri size teslim eder.

def TekCift(num):
    return  num % 2 == 0

my_nums = [1,2,3,4,5,6,7,8,9,10]
liste = list(filter(TekCift, my_nums))
print(liste)


for n in filter(TekCift, my_nums):
    print(n)