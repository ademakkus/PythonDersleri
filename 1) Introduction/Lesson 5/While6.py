# Dışarıdan girilen sayıların birbiriyle olan toplam değerini teslim eden uygulama (123 = 6)
# 123
gelen = input("Lütfen sayısal veri giriniz : ")
index  = 0
result = 0
while index < len(gelen):
    result += int(gelen[index])
    index = index + 1

print(result)