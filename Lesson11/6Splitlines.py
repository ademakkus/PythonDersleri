
#.splitlines() => her bir alt satırdaki elemanların aralarına [,] karakteri ekler
# Not : metin altta yer alan örnek gibi yazıldıysa geçerlidir.

metin = """Bilge
Adam
Beşiktaş
Yazılım
Python
Dersleri
"""

print(metin.splitlines())
#['', 'Bilge', 'Adam', 'Beşiktaş', 'Yazılım', 'Python', 'Dersleri']
# ['Bilge', 'Adam', 'Beşiktaş', 'Yazılım', 'Python', 'Dersleri']


# eğer parametre olarak sonuna True eklerseniz :) aralarına [\n] ekler.

print(metin.splitlines(True))
# ['Bilge\n', 'Adam\n', 'Beşiktaş\n', 'Yazılım\n', 'Python\n', 'Dersleri\n']
