# 1 ile 1000 arasında yer alan sayıların birbirine toplamını ekrana yazdırınız

def Hesapla():
    toplam = 0
    for sayi in range(1,1001):
        toplam += sayi
    print(toplam)

Hesapla()
# 500500