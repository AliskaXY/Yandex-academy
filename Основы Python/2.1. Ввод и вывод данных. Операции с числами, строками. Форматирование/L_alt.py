# Этот вариант ближе к материалу главы

n = int(input())
m = int(input())
a = (int(n // 100) + int(m // 100)) % 10
b = (int(n // 10 % 10) + int(m // 10 % 10)) % 10
c = (int(n % 10) + int(m % 10)) % 10
print(a, b, c, sep='')