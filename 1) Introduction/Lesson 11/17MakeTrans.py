# str.maketrans(), str.translate()
# .str.maketrans(hedef, kaynak) => hedefde verilen karakterleri sırasıyla eşleştirerek, kaynakdaki değerlerle sırasıyla eşleştirir.


kaynak  = "şçöğüıŞÇÖĞÜİ"
hedef   = "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak,hedef)
print(ceviri_tablosu)

# {351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105, 350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}
#  ş    s ,  ç   c , vs.

metin = "Bilge Adam Bireysel Eğitimlerde Artık Python Dersleri Başlayacaktır"
print(metin)
metin = metin.translate(ceviri_tablosu)
print(metin)

#Bilge Adam Bireysel Eğitimlerde Artık Python Dersleri Başlayacaktır
#Bilge Adam Bireysel Egitimlerde Artik Python Dersleri Baslayacaktir