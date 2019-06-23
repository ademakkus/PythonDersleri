# Örnek :  Dışarıdan girilen ürün adına göre, kullanıcıya o ürünün hangi reyonda yer aldığını söyleyen uygulama yazınız.


# Domates, Biber, Patlıcan => Manav Reyonu
# Diş Macunu, Parfüm, Şampuan => Kozmetik Reyonu
# Cep Telefonu, Bilgisayar, Tablet => Teknoloji Reyonu

urun = input("Lütfen ürün adını giriniz : ")
mesaj = "Aradığınız ürün "
if(len(urun)> 0):
    urun = urun.lower()\
        .replace("ş","s")\
        .replace("ı","i")\
        .replace("ğ","g")\
        .replace("ü","u")\
        .replace("ç","c")\
        .replace("ö","o")\
        .replace(" ","")

    if   urun == "domates"       or urun == "biber"      or urun == "patlican":
        mesaj += "Manav Reyonu'ndadır"
    elif urun == "dismacunu"     or urun == "parfum"     or urun == "sampuan":
        mesaj += "Kozmetik Reyonu'ndadır"
    elif urun == "ceptelefonu"   or urun == "bilgisayar" or urun == "tablet":
        mesaj += "Teknoloji Reyonu'ndadır"
    else:
        mesaj += " stoklarımızda yer almamaktadır"

else:
    mesaj = "Lütfen bir ürün adı giriniz!"
print(mesaj)



para = 50
film_ucreti = 20
film_1 = True #"A Filmi"
film_2 = False #"B Filmi"
film_3 = False #"C Filmi"
film_4 = False #"D Filmi"

if para >= film_ucreti and (film_1 or film_2 or film_3 or film_4):
    print("bilet alabilirsin")
else:
    print("Fakir")







