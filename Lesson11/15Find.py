# .find(), .rfind()


metin = "murat vuranok bilge adam beşiktaş yazılım"
sonuc = metin.find("x") # verilen karakteri metin içerisinde soldan sağa doğru arama işlemi yapar. eğer belirtilen karakter metin içerisinde var ise, index değerini, yok ise -1 döner :)
print(sonuc) # 3

sonuc = metin.rfind("x")  # verilen karakteri metin içerisinde sağdan sola doğru arama işlemi yapar. eğer belirtilen karakter metin içerisinde var ise, index değerini, yok ise -1 döner :)

print(sonuc) # 35