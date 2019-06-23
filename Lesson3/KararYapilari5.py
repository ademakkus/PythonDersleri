# Mantıksal operatoler

# and  sorguya katılan her bir koşulun sağlanması durumu
# or   sorguya katılan hergangi bir koşulun sağlanması durumu
# not  sorguya olumsuzluk katar True ise False, False ise True


user_name = input("Lütfen kullanıcı adınızı giriniz : ")
if user_name == "admin":  # db içerisinde varmı ?
    password = input("Lütfen şifrenizi giriniz : ")
    if password == "123":
        print("Giriş yaptınız!")
    else:
        print("Şifreniz yanlış")
else:
    print("Kullanıcı adınız yanlış")
    pass



user_name = input("Lütfen kullanıcı adınızı giriniz : ")
password = input("Lütfen şifrenizi giriniz : ")
if user_name == "admin" and password == "123":
    print( "Tebrikler!")
else:
    print("Kullanıcı bilgilerinizi kontrol ediniz")