petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print('1. Петя')
    if tolya > vasya:
        print('2. Толя')
        print('3. Вася')
    else:
        print('2. Вася')
        print('3. Толя')
elif tolya > vasya and petya < tolya:
    print('1. Толя')
    if petya > vasya:
        print('2. Петя')
        print('3. Вася')
    else:
        print('2. Вася')
        print('3. Петя')
else:
    print('1. Вася')
    if petya > tolya:
        print('2. Петя')
        print('3. Толя')
    else:
        print('2. Толя')
        print('3. Петя')