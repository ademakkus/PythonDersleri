import random








# Kişi Class
class  Person:
    FirstName = "",
    LastName  = "",
    Phone     = "",
    Mail      = ""

 #   def __str__(self):
#       return  "{} {}".format(self.FirstName , self.LastName)


    def Bul(self, kelime):
        if kelime in self.FirstName or \
                kelime in self.LastName or \
                kelime in self.Mail or \
                kelime in self.Phone:
            return  True
        else:
            return  False






# default olarak kullanıcı ekliyoruz.
kisiler = []
isimler = ["Kelly","Harry","Lloyd","Don","Marilyn","Henry","Marcia","Kim","Lena","Delores"]
soyisimler = ["Fleming","Jimenez","Pierce","Howard","Sanchez","Sims","Thomas","Roberts","Nguyen","Torres"]

for i in range(10):
    kisi = Person()
    kisi.FirstName = isimler[random.randint(0,9)]
    kisi.LastName  = soyisimler[random.randint(0,9)].upper()
    kisi.Mail      = "{}.{}@bilgeadam.com".format(kisi.FirstName.lower(),kisi.LastName.lower())
    kisi.Phone     = "+(90) 5{} {} {} {}".format(random.randint(10,100),random.randint(100,1000),random.randint(10,100),random.randint(10,100))

    kisiler.append(kisi)










def Liste(kelime = ""):
    if kelime == "":
        index = 0
        for kisi in kisiler:
            print("-" * 50)
            print(
                "Id           : {}\nKisi Adı     : {}\nKisi Soyadı  : {}\nKisi Telefon : {}\nKisi Mail    : {}".format(
                    index, kisi.FirstName, kisi.LastName, kisi.Phone, kisi.Mail))
            index += 1
    else :
        index = 0
        for kisi in kisiler:
            if kisi.Bul(kelime):
                print("-" * 50)
                print(
                        "Id           : {}\nKisi Adı     : {}\nKisi Soyadı  : {}\nKisi Telefon : {}\nKisi Mail    : {}".format(
                            index, kisi.FirstName, kisi.LastName, kisi.Phone, kisi.Mail))
            index += 1





def Main():
    ekle      = "a"
    sil       = "d"
    guncelle  = "u"
    liste     = "l"
    bul       = "f"
    islem     = ""
    result    = True
    while result:

        print("Lütfen Yapmak Bir İşlem Seçiniz!")
        print("-"*32)
        print("Kişi Eklemek İçin     : a\nKişi Silmek İçin      : d\nKişi Güncellemek İçin : u\nKişi Listesi          : l\nKişi Bulmak İçin      : f")
        print("İşleme Devam Etmek İstemiyorsanız Herhangi Bir Tuşa Basınız!")
        print("-" * 32)
        islem = input("Lütfen Bir Anahtar Kelime Giriniz : ").lower()

        if islem == "a":
            kisi = Person()
            kisi.FirstName = input("Lütfen İsim Giriniz : ")
            kisi.LastName  = input("Lütfen Soyisim Giriniz : ")
            kisi.Phone     = input("Lütfen Telefon Giriniz : ")
            kisi.Mail      = input("Lütfen Mail Giriniz : ")
            kisiler.append(kisi)
            print("Kişi Rehbere Eklendi!")




        elif islem == "d":
            Liste()
            id = int(input("Silmek İstediğiniz Kişinin ID değerini Giriniz! : "))
            kisiler.remove(kisiler[id])
            print("Kişi Rehberden Silindi!")
        elif islem == "u":
            Liste()

            id = int(input("Lütfen Güncellemek İstediğiniz Kişinin ID Değerini Giriniz : "))

            update_person = kisiler[id]

            for key, value in vars(update_person).items():
                vl = input("Lütfen {} Giriniz : " .format(key))
                vars(update_person).__setitem__(key,vl)



            #update_person.FirstName  = input("Lütfen İsim Giriniz : ")
            #update_person.LastName   = input("Lütfen Soyisim Giriniz : ")
            #update_person.Phone      = input("Lütfen Telefon Giriniz : ")
            #update_person.Mail       = input("Lütfen Mail Giriniz : ")

            print("Kişi Rehberde Güncellendi!")
        elif islem == "l":
            Liste()
        elif islem == "f":
            Liste(input("Lütfen Anahtar Kelime Giriniz : "))
        else:
            result = False
            print("Rehber Uygulamasından Çıkış Sağlandı!")


Main()





# Kullanıcı dışarıdan telefon numarası girdiğinde içeride formatlanması
# Metot içerisine telefon numarası alaca, geriye formatlı bir şekilde teslim edecek.
# minimum girilecek değeri 10 hanedir. Eğer kullanıcı eksik deger girerse uyarı verdiriniz.


# 01111111111   => +90(111) 111 11 11
# 1111111111    => +90(111) 111 11 11
# 90111111111   => +90(111) 111 11 11
# +901111111111 => +90(111) 111 11 11