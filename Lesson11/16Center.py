# .center() => nesneye uygulandığında, soldan ve sağdan eşit boşluklar verir
# Not : metinin karakter uzunluğunu verilen değerden çıkartır ve kalan değeri boşluk olarak sola ve sağa dağıtır.

metin = "bilge adam"
print(len(metin))
metin = metin.center(15)
print(metin)
print(len(metin))