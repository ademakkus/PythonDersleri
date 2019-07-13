# Örnek :  //Disaridan siparis alinacak olan kitap miktari girilsin. Sipari sayisi 20'den azsa toplam ucretten %5, 20 - 50 araliginda ise %10, 50-100 araligi ise %15, 100'den fazla ise %25 indirim yapilsin. Kitabın birim fiyatı => 5 TLdir... Amac => Odenecek tutari kullaniciya gostermek...

try:
    birim_fiyat = 5
    siparis_miktari = int(input("Lütfen sipariş adedini giriniz : "))
    toplam_tutar = 0
    mesaj = "Toplamda Ödemeniz Gereken Tutar : "
    if(siparis_miktari > 0):
        if(siparis_miktari <= 20):
            toplam_tutar = (birim_fiyat * siparis_miktari) * 0.95
        elif siparis_miktari >= 20 and siparis_miktari <= 50:
            toplam_tutar = (birim_fiyat * siparis_miktari) * 0.90
        elif siparis_miktari > 50 and siparis_miktari < 100:
            toplam_tutar = (birim_fiyat * siparis_miktari) * 0.85
        elif siparis_miktari > 100:
            toplam_tutar = (birim_fiyat * siparis_miktari) * 0.75
        else:
            mesaj = "Lütfen değerleri kontrol ediniz."

        mesaj += str(toplam_tutar)
        print(mesaj)
    else:
        print("Lütfen 0'dan büyük bir sipariş giriniz!")
except Exception as hata:
    print(hata)

