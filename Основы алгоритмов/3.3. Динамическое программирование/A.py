def FastRocks(n, m):
    if n % 2 == 0 and m % 2 == 0:
        return 'Loose'
    else:
        return 'Win'

n_m = input().split()
print(FastRocks(int(n_m[0]), int(n_m[1])))