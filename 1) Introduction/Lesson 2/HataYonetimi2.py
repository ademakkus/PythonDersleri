try:
    sayi_bir = int(input("Lütfen birinci sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen ikinci sayıyı giriniz : "))

    toplam = sayi_bir + sayi_iki
    fark   = sayi_bir - sayi_iki
    bolum  = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki

    print(  "Sayıların Toplamı :",toplam,
          "\nSayıların Farkı   :",fark,
          "\nSayıların Bölümü  :",bolum,
          "\nSayıların Çarpımı :",carpim )

except (ValueError,SyntaxError):
    print("Value Error veya Syntax Error hatası")
except ZeroDivisionError:
    print("Zero Division Error hatası")
except FileExistsError:
    print("File Exists Error")
except:
    print("hata mesajı")