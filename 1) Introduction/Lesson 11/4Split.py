#.split() => içerisinde verilen parametreye göre soldan sağa doğru ayırma işlemi gerçekleştirir.
elemanlar = "yazılım,sistem,teknik çizim,web grafik"
print(elemanlar)
# yazılım,sistem,teknik çizim,web grafik

elemanlar = elemanlar.split() # => içerisine seperator olarak kullanacağı parametre vermrezseniz default olarak boşluklardan ayıracaktır.
print(elemanlar)

# ['yazılım,sistem,teknik', 'çizim,web', 'grafik']

elemanlar = "yazılım,sistem,teknik çizim,web grafik"
elemanlar = elemanlar.split(',')
print(elemanlar[:])

# ['yazılım', 'sistem', 'teknik çizim', 'web grafik']

 

metin = "murat vuranok yazılım beşiktaş istanbul"
sonuc = metin.split(' ',3)

print(sonuc)
# ['murat', 'vuranok', 'yazılım beşiktaş']
# ['murat', 'vuranok', 'yazılım beşiktaş istanbul']
# ['murat', 'vuranok', 'yazılım', 'beşiktaş istanbul']






