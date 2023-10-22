n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
weight1 = int((n * m - n * k2) / (k1 - k2))
weight2 = n - weight1
print(weight1, weight2)