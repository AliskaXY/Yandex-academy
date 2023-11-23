number = input()

max_num = max(number)
min_num = min(number)
number = number.replace(max_num, '', 1)
number = number.replace(min_num, '', 1)

if int(max_num) + int(min_num) == int(number) * 2:
    print('YES')
else:
    print('NO')