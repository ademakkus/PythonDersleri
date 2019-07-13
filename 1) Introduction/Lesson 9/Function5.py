# Kullanıcı dışarıdan dilediği kadar sayı girecek, her sayı girdikten sonra, sayı girmeye devam edip etmeyeceği sorulacak. :)

# kullanıcı y Y tuşuna basarsa, yeni bir sayı girmesi istenilecek
# kullanıcı harici bir tuşa basar ise, içeriye aldığı sayılar içerindeki tek sayılar içerisinde yer alan en büyü ve en küçün sayının biribirine olan farkını geriye dönecek :)

def FarkHesapla():
    go_on = "y"
    tek_sayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("Lütfen Sayı Giriniz : "))
        if number % 2 != 0:
            tek_sayilar.append(number);
        go_on = input("Yeni bir sayı eklemek istiyormusunuz (Y\\N) : ")

    return max(tek_sayilar) - min(tek_sayilar)

sonuc = FarkHesapla()
print("İşlem Sonucu :",sonuc)
























