from abc import  ABCMeta, abstractmethod

class BasePhone(metaclass = ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, marka, model, fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat


    @abstractmethod
    def Sound(self):
        pass



class Samsung(BasePhone):
    def __init__(self,marka, model,fiyat, tedarikci):
        super(Samsung, self).__init__(marka,model,fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return  "Samsung default mobil phone sound";

class Apple(BasePhone):
    def __init__(self,marka, model,fiyat, garanti):
        super(Apple, self).__init__(marka,model,fiyat)
        self.Garanti = garanti

    def Sound(self):
        return  "Apple default mobil phone sound";


apple = Apple("Apple","8sPlus",10000, "TR")
print("""
Marka        : {}
Model        : {}
Fiyat        : {}
Garanti      : {}  
Telefon Sesi : {}
""".format(apple.Marka, apple.Model, apple.Fiyat,apple.Garanti, apple.Sound()))


samsung = Samsung("Samsung","S10Plus",10000, "KVK")
print("""
Marka        : {}
Model        : {}
Fiyat        : {}
Tedarikçi    : {}  
Telefon Sesi : {}
""".format(samsung.Marka, samsung.Model, samsung.Fiyat,samsung.Tedarikci, samsung.Sound()))


