class Ogrenci:
    """
    self : Sınıf içerisinde yer alan metotların, diğerlerinden farkı hangi sınıf içerisinde çalıştığını belirtmesidir. Self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. Tanımlama yapılırken eklenir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    """
    Adi = ""

    def NotVer(self, ogrenci_not):
        print( self.Adi, "Adlı Öğrenciye {} Notu Verildi!".format(ogrenci_not))

    def CezaVer(self,ogrenci_ceza):
        print( self.Adi, "Adlı Öğrenciye {} Cezası Verildi!".format(ogrenci_ceza))

    def YoklamaGir(self,ogrenci_yoklama):
        print(self.Adi, "Adlı Öğrenci Derse {}!".format(ogrenci_yoklama))


# Kullanım Yöntemleri :
# Class içerisinde tanımlanmış metotlara ulaşma

# 2)
ogrenci = Ogrenci()
ogrenci.Adi ="Murat Vuranok"
ogrenci.NotVer(50)
ogrenci.CezaVer("Disiplin")
ogrenci.YoklamaGir("Geldi")

# Murat Vuranok Adlı Öğrenciye 50 Notu Verildi!
# Murat Vuranok Adlı Öğrenciye Disiplin Cezası Verildi!
# Murat Vuranok Adlı Öğrenci Derse Geldi!

















