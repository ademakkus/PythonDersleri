def Mail(ad:str, soyad:str, domain:str = "bilgeadam") -> str:

    return  "{}.{}@{}".format(ad,soyad,domain)

def Mail1(ad , soyad , domain ) -> str:

    return  "{}.{}@{}".format(ad,soyad,domain)

# Mail("murat","vuranok","hotmail")

# print(type(Mail("","")))
print(Mail("murat","vuranok","hotmail"))
print("Mail metodunun geriye dönüş tipi : ", Mail.__annotations__)
# Mail metodunun geriye dönüş tipi :  {'ad': <class 'str'>, 'soyad': <class 'str'>, 'domain': <class 'str'>, 'return': <class 'str'>}
# murat vuranok bilgeadam
# murat vuranok hotmail


print("Mail metodunun geriye dönüş tipi : ", Mail1.__annotations__)

# Mail metodunun geriye dönüş tipi :  {}
# Mail metodunun geriye dönüş tipi :  {'return': <class 'str'>}