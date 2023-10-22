number = int(input())
a = int(number // 1000)
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
print(b, a, d, c, sep='')