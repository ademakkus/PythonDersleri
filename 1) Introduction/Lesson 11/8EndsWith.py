# .endswith() => metnin parametrede gönderdiğiniz değer ile, bitip bitmediğini sze (True / False) olarak teslim eder

metin = "murat vuranok"
sonuc = metin.endswith("ok")


if sonuc:
    print("metin ok kelimesi ile bitmektedir")
else:
    print("metin ok kelimesi ile bitmemektedir")


# Ternary Kullanımı
print("metin ok kelimesi ile bitmektedir") if sonuc  else print("metin ok kelimesi ile bitmemektedir")

# metin ok kelimesi ile bitmektedir


# sonuc ? "eğer sonut True ise bu bölüm" : "sonuc False geliyor ise bu bölüm"

result = ""
if sonuc:
    result= ""
else:
    result = "me"
print("metin ok kelimesi ile bitme{}ktedir".format(result))
