number = input()

max_num1 = max(number)
max_num2 = max(number.replace(max_num1, '', 1))
min_num1 = min(number)
min_num2 = min(number.replace(min_num1, '', 1))

if min_num1 != '0':
    print(min_num1 + min_num2, max_num1 + max_num2)
else:
    print(min_num2 + min_num1, max_num1 + max_num2)