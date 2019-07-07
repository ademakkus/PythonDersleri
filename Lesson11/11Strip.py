# .strip() => metin başındaki veya sonundaki karakteri silmek için kullanılır.
metin = " bilge adam "
print(metin)
print(len(metin))

metin = metin.strip() # soldaki ve sağdaki boşlukları siler
print(metin)
print(len(metin))

metin = " bilge adam "
metin = metin.lstrip() # soldaki boşluğu siler
print(len(metin))


metin = " bilge adam "
metin = metin.rsplit() # sağdaki boşluğu siler

print(len(metin))