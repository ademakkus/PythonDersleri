# .append() dizi içerisine eleman eklemek için kullanılır. (JavaScript dilindede aynı yöntem geçerlidir.)
# .append() ekleme işlemine dizinin sonundan başlar, eklelen her bir eleman dizinin son elemanıdır.

sehirler =  []

sehirler.append("Ankara")
# bu alana insert yapacak.
sehirler.append("İstanbul")
sehirler.append("Edirne")
sehirler.append("İstanbul")
sehirler.append("İzmir")
sehirler.append("Malatya")

print(sehirler[:])


# .insert() dizinin içerisinde belirtilen alana ekleme işlemi yapar, (araya eleman ekleme)

sehirler.insert(1,"Sivas")

# 1. Parametre hangi index değerine ?
# 2. Parametre o index değerine hangi eleman eklenecek ?
print(sehirler[:])


# ----------------------------------------------



# .count() dizi içerisinde yer alan elemanların, liste içerisinde kaç defa geçtiğini teslim eder

print("Dizi içerisinde İstanbul", sehirler.count("İstanbul"),"adet içermektedir")
# Dizi içerisinde İstanbul 2 adet içermektedir


# ----------------------------------------------



# .pop() dizi içerisinden eleman silme, parametre verilirse, verilen index değerindeki elemanı siler, parametre verilmez ise dizinin en son elemanını siler.

# .pop() metodunun özelliği silinen elemanı geriye teslim eder.

print(sehirler[:])
# print(sehirler.pop(1))
print(sehirler[:])


# ['Ankara', 'Sivas', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir', 'Malatya']
# Sivas
# ['Ankara', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir', 'Malatya']

print(sehirler[:])
print(sehirler.pop())
print(sehirler[:])



# ['Ankara', 'Sivas', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir', 'Malatya']
# Malatya
# ['Ankara', 'Sivas', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir']



# ----------------------------------------------


# .remove() dizi içerisinden eleman silme, eleman silmek için objext olarak nesne ister (pop index mantığı ile remove ise, object mantığı ile çalışır)
# Index değeri üzerinden elaman silme işlemi gerçekleştirmez. Eğer içeride aynı değere sahip (2 adet istanbul gibi) eleman var ise, soldan sağa doğru bulduğu ilk elemanı silecektir.
# .remove() metodu, geriye silinen elemanı teslim etmez!!!


print(sehirler[:])
print(sehirler.remove("İstanbul"))
print(sehirler[:])


# ----------------------------------------------


# .sort() dizinin elemanlarını A'dan Z'ye > 0'dan 9'a sıralama işlemi yapar


print(sehirler[:])
sehirler.sort()
print(sehirler[:])


# ['Ankara', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir', 'Malatya']
# ['Ankara', 'Edirne', 'Malatya', 'İstanbul', 'İstanbul', 'İzmir']


# ----------------------------------------------

# .reverse() dizi içerisindeki elemanları tersine çevirir, kesinlikle  sıralama işlemi yapmaz. diziyi olduğu gibi terten yazdırır.

print(sehirler[:])
sehirler.reverse()
print(sehirler[:])

# ['Ankara', 'İstanbul', 'Edirne', 'İstanbul', 'İzmir', 'Malatya']
# ['Malatya', 'İzmir', 'İstanbul', 'Edirne', 'İstanbul', 'Ankara']



# ----------------------------------------------


print(len(sehirler))
print(sehirler[:])

del sehirler # sehirler dizisini tamamen siler, artık sonraki kod bloklarında bi elemana ulaşamazsınız!

print(len(sehirler))
print(sehirler[:])

























