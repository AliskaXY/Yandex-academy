n = f"{input():0>3}"
m = f"{input():0>3}"
a = (int(n[0]) + int(m[0])) % 10
b = (int(n[1]) + int(m[1])) % 10
c = (int(n[2]) + int(m[2])) % 10
print(a, b, c, sep='')