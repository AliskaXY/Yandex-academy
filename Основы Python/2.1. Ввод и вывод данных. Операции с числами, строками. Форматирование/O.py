n = int(input())
m = int(input())
t = int(input())
minites = (m + t % 60) % 60
hours = (n + t // 60 + (m + t % 60) // 60) % 24
print(f'{hours:0>2}:{minites:0>2}')