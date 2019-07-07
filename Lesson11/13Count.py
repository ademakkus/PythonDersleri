# .count() => metin yada dizi içerisinde parametrede verilen değerin, adet bilgisini teslim eder.

metin = "bilge adam beşiktaş"
sonuc = metin.count("b")
print("metin içerisinde toplamda verdiğiniz parametre {} adet içermektedir".format(sonuc))


metinler = ["ankara","edirne","istanbul","ankara","eskişehir"]

result = metinler.count("ankara")
print(result) # 2


metin = "murat vuranok"
sonuc = metin.count("u") # => 2
print(sonuc)
sonuc = metin.count("u",2) # => 1   2. parametrede verilen değer, başlangın index değeridir. arama işlemine 2. index'ten başla
print(sonuc)

metin = "bilge adam beşiktaş yazılım dersleri, klima ön tarafı soğutmasada arkada kış ayları estirmektedir."



sonuc = metin.count('a')
print("Toplam a karekterinin metin içerisindeki adedi :",sonuc)

sonuc = metin.count('a',6,20) # => a karakterini 6. index değerinden başlayarak 20. index değerine kadar ara
print("Toplam a karekterinin metin içerisindeki adedi :",sonuc)












