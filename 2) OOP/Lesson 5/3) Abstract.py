from abc import  ABCMeta, abstractmethod

class BaseClass(metaclass= ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def printHam(self):
        pass

class Personel(BaseClass):
    def printHam(self):
        return  "personel sesi"


per = Personel()
print(per.printHam())





