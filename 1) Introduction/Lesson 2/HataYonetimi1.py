# Programcı hataları (Error)
# Program kusurları  (Bug)
# İstisnalar         (Exception)
# Mantılsal hatalar
print("sad")


try:
    telefon_numarasi = input("Lütfen telefon numaranızı giriniz : ")
# Telefon numarası veri tabanına kaydedildi
    print("Telefon numaranız :",int(telefon_numarasi))
except ValueError:
    print("İşlem hatası")
    print("Lütfen geçerli bir sayı giriniz")
except ZeroDivisionError:
    print("İşlem hatası")
    print("sıfıra bölünme hatası")


