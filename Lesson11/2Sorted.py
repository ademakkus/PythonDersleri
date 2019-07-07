# sorted() => dizi içerisinde yer alan elemanları A'dan Z'ye, 0'dan 9'a sıralam yapar.



sonuc = sorted("bilgeadam")
print(sonuc)
# ['a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm']




# Türkçe karakterleri dizinin en sonuna atar.


sonuc = sorted("bilgeadamğüişçö")
print(sonuc)

# ['a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm', 'ç', 'ğ']
# alfabetik sıraya göre değil Ascii kod üzerinden devam eder. düzeltmek için.

import  locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")#Windows için
# locale.setlocale(locale.LC_ALL,"tr_TR") # GNU\Linux için


sonuc = sorted("bilgeadamğüişçö", key=locale.strxfrm)
print(sonuc)


# ['a', 'a', 'b', 'd', 'e', 'g', 'i', 'i', 'l', 'm', 'ç', 'ö', 'ü', 'ğ', 'ş']
# ['a', 'a', 'b', 'ç', 'd', 'e', 'g', 'ğ', 'i', 'i', 'l', 'm', 'ö', 'ş', 'ü']