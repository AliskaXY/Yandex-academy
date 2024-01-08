def hanoi_4pegs_steps(n):
    if n == 2:
        return 3
    elif n == 1:
        return 1
    elif n <= 0:
        return -1
    else:
        return  min(7 + 2 * hanoi_4pegs_steps(n-3), hanoi_4pegs_steps(n-4) * 2 + 15)

n = int(input())
print(hanoi_4pegs_steps(n))