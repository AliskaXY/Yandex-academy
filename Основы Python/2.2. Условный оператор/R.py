sides = [int(input()), int(input()), int(input())]

max_side = max(sides)
sides.remove(max_side)

if max_side ** 2 == sides[0] ** 2 + sides[1] ** 2:
    print('100%')
elif max_side ** 2 > sides[0] ** 2 + sides[1] ** 2:
    print('велика')
else:
    print('крайне мала')