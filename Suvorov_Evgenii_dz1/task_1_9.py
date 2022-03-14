a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a < b < c:
    print(f'Среденее число {b}')
elif a < c < b:
    print(f'Среденее число {c}')
else:
    print(f'Среденее число {a}')
