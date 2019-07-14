
# Ogrenci            : isim, soyisim, okul_numarası, TCKN, sınıf, mail, telefon
# Ogretmen           : isim, soyisim,              , TCKN, sınıf, mail, telefon, maas, brans
# Mudur Yardimcisi   : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
# Mudur              : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
# Memur              : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
# Hizmetli           : isim, soyisim,              , TCKN,      ,     , telefon, maas, gorev


class BaseClass:
    isim          = ""
    soyisim       = ""
    TCKN          = ""
    mail          = ""
    telefon       = ""

    def __str__(self):
        return  "{} {}".format(self.isim, self.soyisim)


class Calisan(BaseClass):
    maas = ""
    gorev = ""

 
class Ogrenci(BaseClass):
    okul_numarası = ""
    sinif         = ""

class Ogretmen(BaseClass):
    sinif         = ""
    maas          = ""
    brans         = ""

class MudurYardimcisi(Calisan):
    pass

class Mudur(Calisan):
    pass

class Memur(Calisan):
    pass

class Hizmetli(Calisan):
    pass























ogrenci = Ogrenci()
ogrenci.isim = "murat"
ogrenci.soyisim = "vuranok"
ogrenci.TCKN = 24324234
ogrenci.mail = ""

print(ogrenci)


mudur = Mudur()
mudur.ma
