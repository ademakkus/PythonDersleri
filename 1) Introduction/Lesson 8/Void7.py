# Dışarıdan aldığı isim ve soyisime göre mail adresi oluşturan metot
#isim.soyisim@bilgeadam.com

# Kullanıcı 2. parametrede değer göndermeye bilir.

def MailAdres(isim, soyisim = None):
    if soyisim is None:
        mail = "{}@bilgeadam.com".format(isim.lower())
    else:
        mail = "{}.{}@bilgeadam.com".format(isim.lower(),soyisim.lower())
    print(mail)



MailAdres(input("Lütfen Adınızı Girini : "))
MailAdres(input("Lütfen Adınızı Girini : "), input("Lütfen Soyadınızı Giriniz : "))

# MuRat.VURANok@bilgeadam.com
# çağrı.çağırma@bilgeadam.com
# murat.@bilgeadam.com