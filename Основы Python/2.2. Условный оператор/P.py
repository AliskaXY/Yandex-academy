petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print(f'{"Петя": ^24}')
    if tolya > vasya:
        print(f'{"Толя": ^8}')
        print(f'{" ": >16}{"Вася": ^8}')
    else:
        print(f'{"Вася": ^8}')
        print(f'{" ": >16}{"Толя": ^8}')
elif tolya > vasya and petya < tolya:
    print(f'{"Толя": ^24}')
    if petya > vasya:
        print(f'{"Петя": ^8}')
        print(f'{" ": >16}{"Вася": ^8}')
    else:
        print(f'{"Вася": ^8}')
        print(f'{" ": >16}{"Петя": ^8}')
else:
    print(f'{"Вася": ^24}')
    if petya > tolya:
        print(f'{"Петя": ^8}')
        print(f'{" ": >16}{"Толя": ^8}')
    else:
        print(f'{"Толя": ^8}')
        print(f'{" ": >16}{"Петя": ^8}')
print('   II      I      III   ')