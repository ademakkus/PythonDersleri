# Örnek :  Dışarıdan girilen kelimenin uzunluk değeri 8 karakter veya daha uzun bir karekter ise, Onaylandı!, değil ise, Daha uzun bir şifre giriniz.


# len() => var olan değerin size uzunluğunu teslim eder.
parola = len(input("Lütfen şifrenizi giriniz !"))
if parola >= 8:
    print("Tebrikler!")
else:
    print("Budamı gol değil!!!")

