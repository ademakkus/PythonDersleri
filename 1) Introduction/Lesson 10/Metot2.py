


# Metot(Ad, Soyad, Telefon, Gorev):
# Metot(*parametreler):

def Metot(Ad, Soyad, Telefon, Gorev,*par):
    print(Ad,Soyad,Telefon,Gorev,par)


def Metot1(*params):
    for i in params:
        print(i)


Metot("murat","vuranok","53238899123213","Danışman",213,213,123,123,123,123,123)
Metot1("murat","vuranok","53238899123213","Danışman")

# murat vuranok 53238899123213 Danışman
# ('murat', 'vuranok', '53238899123213', 'Danışman')
# (213, 213, 123, 123, 123, 123, 123)

#murat vuranok 53238899123213 Danışman
#murat
#vuranok
#53238899123213
#Danışman
 
def MetotVol1(**params):
    print(params["Ad"])

MetotVol1(
    Ad      = "Murat Vuranok",
    Soyad   = "Vuranok",
    Telefon = "213213213",
    Mail    = "murat.vuranok@bilgeadam.com")




