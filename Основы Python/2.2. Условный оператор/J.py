number = int(input())

sum1 = number % 10 + number // 10 % 10
sum2 = number // 100 + number // 10 % 10

if sum1 > sum2:
    print(sum1, sum2, sep='')
else:
    print(sum2, sum1, sep='')