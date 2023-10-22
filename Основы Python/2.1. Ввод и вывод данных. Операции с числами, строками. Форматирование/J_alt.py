# учитывая материал главы это решение болше подходит к ее содержанию

name = input()
locker = int(input())
group = int(locker / 100)
number = locker % 10
bed = locker // 10 % 10
print(f"Группа №{group}.")
print(f"{number}. {name}.")
print(f"Шкафчик: {locker}.")
print(f"Кроватка: {bed}.")