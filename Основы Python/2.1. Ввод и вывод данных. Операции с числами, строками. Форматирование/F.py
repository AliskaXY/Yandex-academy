product = input()
price = int(input())
weight = int(input())
money = int(input())
cost = price * weight
change = money - cost
print("Чек")
print(f"{product} - {weight}кг - {price}руб/кг")
print(f"Итого: {cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")