# karar yapıları if - elif - else

# Karılaştırma operatorleri

# == (Eşittir) Soldaki değerin, sağdaki değere eşit olma durumu
# Örnek : 1 == 1 Sonuç => True
#         4 == 2 Sonuc => False

# != (Eşit Değildir) Soldaki değerin, sağdaki değere eşit olmama durumu
# Örnek : 1 != 2 Sonuc => True
#         1 != 1 Sonuc => False


# >   (Büyüktür) Soldaki değerin, sağdaki değerden büyük olma durumu
# Örnek : 3 > 1 Sonuc => True
#         1 > 2 Sonuc => False


# <    (Küçüktür) Soldaki değerin, sağdaki değerden küçük olma durumu
# Örnek : 1 < 2 Sonuc => True
#         4 < 1 Sonuc => False



# >=  (Büyük veya Eşit) Soldaki değerin, sağdaki değerden büyük veya eşit olma durumu
# Örnek : 1 >= 1 Sonuc => True (eşitlik)
#         3 >= 2 Sonuc => True (büyüklük)
#         1 >= 2 Sonuc => False


# <=  (Küçük veya Eşit) Soldaki değerin, sağdaki değerden küçük veya eşit olma durumu

# Örnek : 1 <= 1 Sonuc => True (eşitlik)
#         1 <= 3 Sonuc => True (küçüklük)
#         4 <= 1 Sonuc => False




username = input("Lütfen kullanıcı adınızı giriniz : ")
username = username\
    .lower()\
    .replace("ı","i")\
    .replace('̇n','n')\
    .replace("ç","c")\
    .replace("ş","s")\
    .replace("ö","o")\
    .replace("ğ","g")

print(username)
if(username == "admin"):
    print("Giriş yaptınız!")
else:
    print("Kullanıcı adınız hatalı!")




# https://codingbat.com/prob/p173401
# bu alandaki örnekler çözülecek.









