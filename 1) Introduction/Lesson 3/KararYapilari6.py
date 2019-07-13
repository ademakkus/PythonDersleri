# Örnek : Dışarıdan girilen not aralığı
#  0 – 30  =>  FF
# 30 – 50  =>  DD
# 50 – 70  =>  CC
# 70 – 85  =>  BB
# 85 – 100 =>  AA ,  harf notunu aldınız uyarısını kullanıcıya veriniz.

try:
    not_ =  int(input("Lütfen notunuzu giriniz : "))
    mesaj = "Harf notunuz : "
    if  not_  > 0  and not_ <= 30:
        mesaj += "FF"
    elif not_ > 30 and not_ <= 50:
        mesaj += "DD"
    elif not_ > 50 and not_ <= 70:
        mesaj += "CC"
    elif not_ > 70 and not_ <= 85:
        mesaj += "BB"
    elif not_ > 85 and not_ <= 100:
        mesaj += "AA"
    else:
        mesaj = "Geçersiz not girdiniz!"

    print(mesaj)
except Exception as hata:
    print(hata)