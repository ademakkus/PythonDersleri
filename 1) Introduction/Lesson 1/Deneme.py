myfile = open("file.txt")
print(myfile.read())

print(myfile.read()) # 2. okumada boş gelecektir. okuma yaparken cursor'ı en sona attığından son karakteri okumaya çalışır

# öncelikle cursor'ı 0. index'e getirmemiz gerekir.

myfile.seek(0)
print(myfile.read())

myfile.seek(0)

print(myfile.readlines())

# ----------------------------------------------
with open("file.txt") as deneme_file:
    content = deneme_file.read()

print("-"*25)
print(content)









# ---------------------------------------------------


# mode = 'r'  read only
# mode = 'w'  write only ( will overwrite or create new) var ise üzerine yaz, yok ise yeni oluştur
# mode = 'a'  is append only (will add on to files)
# mode = 'r+' is reading and writing
# mode = 'w+' is writing and reading (overwrites existitn files or creates o new file!)






# s = 'hello'
# reverse the string using slicing
# print(s[::-1])












