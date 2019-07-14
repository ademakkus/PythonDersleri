from datetime import datetime
from datetime import timedelta

class Personel:

    FirstName = ""
    LastName  = ""
    Mail      = ""
    Phone     = ""
    # Personelin işe giriş tarihi sistemden, default olarak verilmektedir.
    HireDate  = "{}/{}/{} {}:{}".format(datetime.now().year,
                                        datetime.now().month,
                                        datetime.now().day,
                                        datetime.now().hour,
                                        datetime.now().minute)
    FireDays  = 0
    Address   = ""



    def IseAl(self):
        print("Personel Adı                   : {} \nPersonel Soyadı                : {}\nPersonel Mail                  : {}\nPersonel Telefon               : {}\nPersonel İşe Giriş Tarihi      : {}\nPersonel Adres                 : {}\nPersonel Sözleşme Bitiş Tarihi : {}\nPersonel İşe Girişi Yapıldı!".format(
            self.FirstName,
            self.LastName,
            self.Mail,
            self.Phone,
            self.HireDate,
            self.Address,
            "{}/{}/{} {}:{}".format((datetime.now() + timedelta(days = self.FireDays)).year,
                                    (datetime.now() + timedelta(days = self.FireDays)).month,
                                    (datetime.now() + timedelta(days = self.FireDays)).day,
                                    (datetime.now() + timedelta(days = self.FireDays)).hour,
                                    (datetime.now() + timedelta(days = self.FireDays)).minute)
            ))

    def Guncelle(self):
        # Personel bilgilerini günceleme
        pass
    def Kov(self):
        # Personel'in veri tabanından silinme işlemi
        # Status = 3
        pass


time = datetime.now()

personel = Personel()
personel.FirstName = "Murat"
personel.LastName  = "Vuranok"
personel.Mail      = "murat.vuranok@bilgeadam.com"
personel.Phone     = "+905323334455"
personel.FireDays  = 150
personel.Address   = "İstanbul/Beşiktaş"

personel.IseAl()

