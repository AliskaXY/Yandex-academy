a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif D < 0 or (a == 0 and b == 0):
    print('No solution')
elif a == 0:
    x = - c / b
    print(f'{x:.2f}')
elif D == 0:
    x = (D ** (1 / 2) - b) / (2 * a)
    print(f'{x:.2f}')
else:
    x1 = (D ** (1 / 2) - b) / (2 * a)
    x2 = (0 - D ** (1 / 2) - b) / (2 * a)
    if x1 > x2:
        print(f'{x2:.2f} {x1:.2f}')
    else:
        print(f'{x1:.2f} {x2:.2f}')