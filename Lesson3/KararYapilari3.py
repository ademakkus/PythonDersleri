# Örnek :  Dışarıdan girilen sayının tek veya çift olma durumunun kontrol edilmesi. Eğer sayı tek ise, Kullanıcıya sayı tektir. Çift ise sayı çift’tir uyarısı veriniz.


try:
    sayi = int(input("Lütfen sayı giriniz : "))
    if sayi % 2 == 0:
        print("Girilen sayı çift'tir")
    else:
        print("Girilen sayı tek'tir")
except Exception as hata:
    print(hata)
    print("Sayı girmek ne kadar zor olabilir ?")
