metin = "bilge Adam BEŞİKTAŞ"

print(metin.lower()) # tüm karakterleri küçük harfe çevirir.
print(metin.upper()) # tüm karakterleri büyük harfe çevirir.

# bilge adam beşi̇ktaş
# BILGE ADAM BEŞİKTAŞ


metin  = metin.lower()
result = metin.islower() # tüm karakterlerin küçük olup olmadığını kontrol eder. True / False değeri teslim eder.
print(result) # => True


result = metin.isupper() # tüm karakterlerin büyük olup olmadığını kontrol eder. True / False değeri teslim eder.
print(result)   # => False