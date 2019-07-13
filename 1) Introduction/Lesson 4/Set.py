# set()   : uniq olarak içerisinde veri tutar, aynı veriyi ekleyebilirsini fakat size dataları tekil olarak teslim eder.

myset = set()

print(myset)

myset.add(1)

print(myset)

myset.add(2)
myset.add(2)
myset.add(2)

print(myset)

mylist= [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

print(mylist)

print(set(mylist))