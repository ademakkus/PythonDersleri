# Örnek 1) Disaridan alinan iki sayının toplamiyla farkinin birbirine bolumunden kalanin sonucu kactir?
#(Farkın toplama bolumunden kalan kactir?)

#sayi_bir = int(input("birinci sayi : "))
#sayi_iki = int(input("ikinci sayi : "))

#sayi_toplam = sayi_bir + sayi_iki
#sayi_fark   = sayi_bir - sayi_iki
#sayi_mod    = sayi_toplam % sayi_fark
#print("islem sonucu : ", sayi_mod)

# -------------------------------------------------------------------------------------------------------------

# Örnek 2) Disaridan girilen bir sayının 10 eksiginin 20 fazlasinin 2ye bolumunden kalaninin karesi kactir?


#sayi = int(input("lutfen sayi giriniz"))

#sonuc = ((sayi - 10 + 20 ) % 2) ** 2
#print("islem sonucu :",sonuc)

#kare = sonuc * sonuc
#print("islem sonucu :",kare)

# ** kuvvet alma




# Örnek 3) Disaridan girilen iki sayının karelerinin toplami ile karelerinin farki toplami kactir?


#sayi1 = int(input("lutfen birinci sayiyi giriniz : "))
#sayi2 = int(input("lutfen ikinci sayiyi giriniz : "))

#kare1 = sayi1 * sayi1
#kare2 = sayi2 * sayi2
 
#kare11 = sayi1**2
#kare22 = sayi2**2


#toplam = kare1 + kare2
#fark = kare1 - kare2

#sonuc = toplam + fark
#print ("islem sonucu :", sonuc)
 
# Örnek 4) Vize notu'nun % 30'u, final notu'nun % 70'ini alıp öğrencinin not ortalamasini cikartan bir uygulama yaziniz...
# DİKKAT => Notlar ondalikli olabilir?


#not_vize = float(input("vize notunuzu giriniz : "))
#not_final = float(input("final notunuzu giriniz : "))

#sonuc = (not_vize * 0.30) + (not_final * 0.70)
#print("Toplam notunuz :",sonuc)

 

# Örnek 5) Kullanıcı ilk Adını, 2. Olarak Soyadını girsin ve kullanıcıya mesaj olarak isim.soyisim@hotmail.com


isim = input("lutfen isiminizi giriniz : ")
soyisim = input("lutfen soyisminizi giriniz : ")

print("{}.{}@hotmail.com".format(isim,soyisim))
print(isim,".",soyisim,"@hotmail.com")

# murat . vuranok @hotmail.com
mail = isim+"."+soyisim+"@hotmail.com"
# murat.vuranok@hotmail.com
# {}.{}@hotmail.com

mail_ = "{}.{}@hotmail.com".format(isim, soyisim)
























