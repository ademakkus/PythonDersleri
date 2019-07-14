class Employee:
    """
Personel Tanımlama
Personeli Tanımla :)
    """
    FirstName  = ""
    LastName   = ""
    Department = ""
    Mail       = ""
    Phone      = ""

# Employee sınıfından instance(yeni bir örnek almak :) ) alma
personel = Employee()


personel.Mail       ="murat.vuranok@bilgeadam.com"
personel.Department = "Yazılım"
personel.FirstName  = "Murat"
personel.LastName   = "Vuranok"

print(personel)
# <__main__.Employee object at 0x03541E50>
# eğer sınıfı direkt olarak yazdırırsak bize, o sınıfın adı ve heap üzerindeki adresini teslim eder.

print(personel.LastName)




























