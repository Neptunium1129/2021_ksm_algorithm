#그리디 거스름돈
#n이 1260이라 가정
n = 1260
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)
