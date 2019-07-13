# 10 eşittir 2 * 5
# 11 asal sayıdır
# 12 eşittir 2 * 6
# 13 asal sayıdır
# 14 eşittir 2 * 7
# 15 eşittir 3 * 5
# 16 eşittir 2 * 8
# 17 asal sayıdır
# 18 eşittir 2 * 9
# 19 asal sayıdır
# 20 eşittir 2 * 10

# range(10,20)



for num in range(10,21):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print("{} eşittir {}*{}".format(num,i, int(j)))
            break
    else:
        print(num, "Asal sayıdır")


#10 eşittir 2*5
#11 Asal sayıdır
#12 eşittir 2*6
#13 Asal sayıdır
#14 eşittir 2*7
#15 eşittir 3*5
#16 eşittir 2*8
#17 Asal sayıdır
#18 eşittir 2*9
#19 Asal sayıdır
#20 eşittir 2*10






















