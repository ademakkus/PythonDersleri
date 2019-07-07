def decorator_metot(metot):
    def  sarmal_metot():
        print("Sarmal metodu {}'dan önce tetiklendi"
              .format(metot.__name__))
        return  metot()
    return  sarmal_metot


@decorator_metot
def Print_Metot():
    print("Print_Metot çalıştı")

Print_Metot()


#Sarmal metodu Print_Metot'dan önce tetiklendi
#Print_Metot çalıştı
