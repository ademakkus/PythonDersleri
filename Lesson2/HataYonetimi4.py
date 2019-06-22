try:
    sayi_bir = int(input("Lütfen bölünecek sayıyı giriniz : "))
    sayi_iki = int(input("Lütfen bölecek olan sayıyı giriniz : "))
    sonuc = sayi_bir / sayi_iki

except ValueError as exp:
    print("İşlem hatası :",exp)
else:
    try:
        print(sayi_bir/sayi_iki)
        print(sonuc)
    except ZeroDivisionError:
        print("Sayı 0 değerine bölünemez!")