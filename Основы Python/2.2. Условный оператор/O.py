num1 = input()
num2 = input()

num1_max = max(num1)
num1_min = min(num1)
num2_max = max(num2)
num2_min = min(num2)

if num1_max >= num2_max:
    max_num = num1_max
    remainder1 = int(num2_max)
else:
    max_num = num2_max
    remainder1 = int(num1_max)

if num1_min >= num2_min:
    min_num = num2_min
    remainder2 = int(num1_min)
else:
    min_num = num1_min
    remainder2 = int(num2_min)

middle_num = str((remainder1 + remainder2) % 10)
print(max_num + middle_num + min_num)