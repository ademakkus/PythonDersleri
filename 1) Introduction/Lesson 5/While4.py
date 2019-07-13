# 1 ile 1000 arasında yer alan tek ve çift sayıların adedini ekrana yazdırınız :)

index = 1
tekSayilarinToplami = 0
ciftSayilarinToplami = 0

while index <= 1000:
    if index % 2 == 0:
        ciftSayilarinToplami = ciftSayilarinToplami + 1
    else:
        tekSayilarinToplami = tekSayilarinToplami + 1
    index = index + 1


print("Tek sayıların toplamı :",tekSayilarinToplami, "\nÇift sayıların toplamı :",ciftSayilarinToplami)
