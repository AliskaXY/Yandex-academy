def steps(n):
    if n == 1:
        return 1
    else:
        return 2 * steps(n - 1) + 1

   
def hanoi_towers(n, from_peg, to_peg):
    if n == 1:
        print(from_peg, to_peg)
    else:
        unused_peg = 6 - from_peg - to_peg
        hanoi_towers(n - 1, from_peg, unused_peg)
        print(from_peg, to_peg)
        hanoi_towers(n - 1, unused_peg, to_peg)

   
n = int(input())
print(steps(n))
hanoi_towers(n, 1, 3)