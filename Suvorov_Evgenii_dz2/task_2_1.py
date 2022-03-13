while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    oper = input('Введите математический оператор ("+","-", "/", "*"): ')
    if oper == '+':
        print(f'Результат вычисления = {a + b}')
    elif oper == '-':
        print(f'Результат вычисления = {a - b}')
    elif oper == '*':
        print(f'Результат вычисления = {a * b}')
    elif oper == '/':
        if b != 0:
            print(f'Результат вычисления = {a / b}')
        else:
            print('Деление на ноль!')
    elif oper == "0":
        break
    else:
        print('Введен неверный оператор')