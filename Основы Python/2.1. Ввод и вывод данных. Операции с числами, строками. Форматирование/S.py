product = input()
price = int(input())
weight = int(input())
money = int(input())
cost = price * weight
change = money - cost
print(f"{'Чек':=^35}")
print(f"Товар:{product: >29}")
print(f"Цена:{f'{weight}кг * {price}': >24}руб/кг")
print(f"Итого:{cost: >26}руб")
print(f"Внесено:{money: >24}руб")
print(f"Сдача:{change: >26}руб")
print("=" * 35)