while True:
    sifre = input("Lütfen şifre giriniz : ")
    if not sifre:
        pass
    elif len(sifre) in range(3,8):
        print("yeni şifreniz :", sifre)
        break
    else:
        print("şifre 3 ile 8 karakter aralığında olmalıdır.")