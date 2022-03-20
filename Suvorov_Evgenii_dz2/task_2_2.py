a = input('Введите целое число: ')
even_count = 0
not_even_count = 0
for el in a:
    if int(el) % 2 == 0:
        even_count += 1
    else:
        not_even_count += 1
print(f'Кол-во четных цифр {even_count = }\nКол-во нечетных цифр {not_even_count = }')
