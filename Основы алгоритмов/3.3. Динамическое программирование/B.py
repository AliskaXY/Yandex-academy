import time
start_time = time.time()

def Rocks(n, m):
    W = 'Win'
    L = 'Loose'
    R = [
        [L, W],
        [W, L],
    ]
    if n != 1 and m != 1:
        for i in range(2, n+1, 1):
            if R[0][i-1] == W and R[0][i-2] == W:
                R[0].append(L)
            else:
                R[0].append(W)
            if R[1][i-1] == W and R[1][i-2] == W and R[0][i-2] == W:
                R[1].append(L)
            else:
                R[1].append(W)
        for j in range(2, m+1, 1):
            if R[j-1][0] == W and R[j-2][0] == W:
                R.append([L])
            else:
                R.append([W])
            if R[j-1][1] == W and R[j-2][1] == W and R[j-2][0] == W:
                R[j].append(L)
            else:
                R[j].append(W)
        for j in range(2, m+1, 1):
            for i in range(2, n+1, 1):
                if R[j][i-1] == W and R[j-1][i] == W \
                    and R[j][i-2] == W and R[j-2][i] == W \
                    and R[j-1][i-2] == W and R[j-2][i-1] == W:
                    R[j].append(L)
                else:
                    R[j].append(W)
    return R[m][n]

n_m = input().split()
print(Rocks(int(n_m[0]), int(n_m[1])))

end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения программы: ", execution_time, "секунд")