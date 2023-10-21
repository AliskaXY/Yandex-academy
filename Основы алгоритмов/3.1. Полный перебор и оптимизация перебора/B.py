def factorial(n):
    ans = 1
    for i in range(n):
        ans = ans*(i+1)
    return ans

cnk = input()
cnk = cnk.split()
out = int(factorial(int(cnk[0]))/factorial(int(cnk[1]))/factorial(int(cnk[0])-int(cnk[1])))
print(out)