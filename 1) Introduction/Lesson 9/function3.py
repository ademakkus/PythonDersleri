# Disaridan girilen ilk kelimenin ilk iki harfini buyuk,
# geri kalanini kucuk aliniz..
# ikinci kelimenin icerisinde gecen tum a'lari e'ile degistiriniz
# ve sonuna @hotmail.com ekleyerek geri dondurunuz...

def Mail(isim, soyisim):
    isim_    = isim[0:2].upper() + isim[2:].lower()
    soyisim_ = soyisim.replace("a","e")
    return  "{}.{}@hotmail.com".format(isim_, soyisim_)

mail = Mail("muRAT","vuranok")
print("Kullanıcı Mail Adresini :", mail)
