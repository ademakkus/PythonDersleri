a = 40  # Değeri 40 olan sayısal bir <class 'int'> tipinde bir değişken tanımladık

b = a   # b değişkeni tanımlayıp referansını a değişkeninden aldık.
c = [b] # c değişkeni tanımlayıp <class 'list'> b değerini referans olarak verdik.

# print(type(a))
# print(a)

del a           # a değişkeninin referansını sildik
b = 100         # b değerine 100 değerini vererek üzerinde yer alan 40 değerini değiştirdik.
# print(type(c))
c[0] =-1        # c listesinin 0. elemanının değerini -1 olarak değiştirere 40 değerini sildik ve a değişkenine ait hiç bir referans kalmamıştır.

# print(c[0])






class Point:
    def __init__(self , x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Heap üzerinden silindi")



pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1), id(pt2), id(pt3))  # nesnenin ram adresi değerinin ekrana yazdırılması
# pt1 => 24518256
# pt2 => 24518256
# pt3 => 24518256

del  pt1
del  pt2
del  pt3


# id() Nesnenin kimliğini döndürür. Nesne yaşam ömrü boyunca benzersiz be sabit olacağı garantilenen (uniq) bir tam sayıdır. birbirinden benzersiz iki nesne aynı değere sahip olabilirler.