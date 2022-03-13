from random import randint

a = randint(0, 100)
print('Угадайте число за 10 попыток')
i = 1
while i <= 10:
    user_answer = int(input(f'Попытка №{i}: '))
    if user_answer == a:
        print('Победа!')
        break
    elif user_answer < a:
        print('Введенное число меньше загаданного.')
    elif user_answer > a:
        print('Введенное число больше загаданного.')
    i += 1
if i > 10:
    print(f'Правильный ответ - {a}')
