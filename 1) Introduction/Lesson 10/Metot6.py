#def square(num):
#    result = num **2
    #   return  result

#def square(num):
#    return  num**2

#def square(num): return  num**2 # Hatalı kullanım

# lamda kullanımı

square = lambda  num : num **2
print(square(5))
my_nums = [1,2,3,4,5,6,7,8,9]

result = list(map(lambda  num : num**2,my_nums))
print(result)

result = list(filter(lambda  num : num % 2 == 0,my_nums))
print(result)