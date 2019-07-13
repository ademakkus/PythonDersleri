# dışarıdan girilen metni harf harf alt alta yazdırınız :)

metin = input("lütfen bir metin giriniz! : ")
result = ""
for karakter in metin:
    result += karakter +"-"
print(result)


print("-".join(metin))