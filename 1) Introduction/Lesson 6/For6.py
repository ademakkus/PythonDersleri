# şifrenin 3 defa yanlış girilmesi dahilinde kullanıcıyı uyaran uygulama
from builtins import print

for i in range(3):
    parola = input("Şifrenizi Giriniz : ")
    if i == 2:   # şifre 3 defa yanlış girildi
        print("Şifrenizi 3 defa yanlış girdiniz!!!")
    elif not parola: # alan boş geçilirse
        print("Parola boş geçilemez!!!")
    elif len(parola) in range(3,8): # parola 3 ile 8 karakter aralığında olmalıdır.
        print("Parolanız :", parola,"Olarak Belirlenmiştir!")
        break
    else:
        print("Naptında bu mesajı aldın ?")