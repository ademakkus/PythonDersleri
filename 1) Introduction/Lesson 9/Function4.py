# Disaridan bir sayısal dizisinin parametre olarak alan bir metot yaziniz. Metot, parametredeki dizide yer alan elemanlarin toplaminin karekökünü dondursun...

import  math   # import anahtar kelimesi, içeride var olan herhangi bir kütüphaneyi eklemek için kullanıyoruz.

def KarekokHesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return  math.sqrt(toplam)

sonuc = KarekokHesapla([1,2,3,4,5,6,7,8,9,9,7,5,33,44,55,7234,324])
print("İşlem sonucu : ", sonuc)

# İşlem sonucu :  88.06815542521599