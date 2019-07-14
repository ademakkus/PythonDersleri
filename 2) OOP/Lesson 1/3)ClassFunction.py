class Ogrenci:
    """
    self : Sınıf içerisinde yer alan metotların, diğerlerinden farkı hangi sınıf içerisinde çalıştığını belirtmesidir. Self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. Tanımlama yapılırken eklenir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    """
    Adi = ""

    def NotVer(self, ogrenci_not):
        print(ogrenci_not,  "Adlı Öğrenciye Not Verildi!")

    def CezaVer(self,ogrenci_ceza):
        print(ogrenci_ceza,  "Adlı Öğrenciye Ceza Verildi!")

    def YoklamaGir(self,ogrenci_yoklama):
        print(ogrenci_yoklama,  "Adlı Öğrencinin Yoklaması Girildi!")


# Kullanım Yöntemleri :

# Class içerisinde tanımlanmış metotlara ulaşma
# 1)
# Ogrenci.NotVer("", "Murat Vuranok" )
# Ogrenci.CezaVer("","Murat Vuranok"  )
# Ogrenci.YoklamaGir("","Murat Vuranok"  )
# ----------------------------------------------------------------------



















