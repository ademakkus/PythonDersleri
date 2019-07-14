class Calisan():
    def __init__(self, isim, soyisim, maas, departman, yas = 10):
        print("Çalışan sınıfının yapıcı metodu çalıştı!")
        self.isim      = isim
        self.soyisim   = soyisim
        self.yas       = yas
        self.maas      = maas
        self.departman = departman

    def __str__(self):
        return "{} {} {}".format(
            self.isim,
            self.soyisim,
            self.yas)

    def BilgiGoster(self):
        print("Çalışan Sınıfına Ait Bilgiler Gösterilmektedir!")
        print("-"*30)
        print("- İsim      : {}\n- Soyisim   : {}\n- Departman : {}\n- Maaş      : {}".format(
            self.isim,
            self.soyisim,
            self.departman,
            self.maas))
        print("-" * 30)

    def ZamYap(self,zam_orani):
        print("Çalışanın Maaşına Zam Yapıldı!")
        maas_  = self.maas
        self.maas += zam_orani
        print("{} Personelinin Maaşı : {} TL den {} TL ye Yükseltildi.".format(self.isim + " "+ self.soyisim,maas_,self.maas))


    def DepartmanDegistir(self, departman):
        print("Çalışanın Departmanı Değiştirldi!")
        departman_ = self.departman
        self.departman = departman
        print("{} Personelinin Departmanı : {} departmanından {} Departmanına Geçişi Sağlandı".format(self.isim + " " + self.soyisim, departman,self.departman))



# personelin maaşına zam yapıldığında veya departmanı değiştirildiğinde, kullanıcıya eski değer ve yeni değerleri gösteriniz.



# X Personelinin Departmanı : X departmanından Y Departmanına Geçişi Sağlandı
# X Personelinin Maaşı      : X TL den Y TL ye Yükseltildi.



# yas parametresi göndermezsek, içeride tanımlı default değer geçerli olacaktır.


# personel = Calisan("murat","vuranok",5000,"yazılım")
#personel = Calisan("murat","vuranok",5000,"yazılım",98)
#print(personel)
#personel.BilgiGoster()
#personel.ZamYap(1000)
#personel.DepartmanDegistir("sistem")






class Yonetici(Calisan):  # yönetici sınıfına çalışan sınıfını miras veriyoruz.
    def __init__(self,isim, soyisim, maas, departman,yas, kisi_sayisi):
        print("Yönetici sınıfı, yapıcı metodu çalıştı!")
        self.isim        = isim
        self.soyisim     = soyisim
        self.departman   = departman
        self.maas        = maas
        self.kisi_sayisi = int(kisi_sayisi)
        self.yas         = yas

    def prin_base(self):
        for base in self.__class__.__bases__:
            print("Miras Alınan Sınıf : ", base.__name__)

    def __str__(self):
        return  "{} {} {}".format(self.isim, self.soyisim,self.departman)





yonetici = Yonetici("Ahmet","Mehmet",9000,"sistem",35,20)
print(yonetici)
yonetici.prin_base()
yonetici.BilgiGoster()
yonetici.ZamYap(1500)
yonetici.DepartmanDegistir("yazılım")

























