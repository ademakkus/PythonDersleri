from  enum import  Enum

class RenkEnum(Enum):
    Kırmızı = 1
    Sarı = 2
    Mavi = "Blue"
    Mail = "Mail Adresi, @ işareti içermelidir. Lütfen kontrol ediniz"

print(repr(RenkEnum.Mavi)) # <RenkEnum.Mavi: 'Blue'>
print( RenkEnum.Mail.value )


class IntEnum(int, Enum):  # birinci parametrede verilen veri tipi ne ise, içeride tanımladığınız value değeride o tipte olmak zorundadır.
    Kırmızı = 1
    Sarı    = 2
    # Mavi    = "Mavi"

print(IntEnum.Kırmızı)

class floatEnum(float, Enum):
    Kırımızı = 1
    Mavi = 2
    Yeşil = 1.10

print(floatEnum.Yeşil.value)