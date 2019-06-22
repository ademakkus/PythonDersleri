# Hata mesajı

try:
    sayi = int(input("Lütfe sadece sayısal veri giriniz : "))
    print("gelen sayı", sayi)
    #sayi = sayi / 0
    sayi = str(sayi) / 0
    print("İşlem sonu")

except ValueError as ex:
    print("ValueError")
    print("Sistem hata mesajı ",ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("Sistem hata mesajı ",ex)
except Exception as ex:
    print("except")
    print("Sistem hata mesajı ",ex)