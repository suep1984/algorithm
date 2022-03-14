a = list(input('Введите трэхзначное число: '))
res_mul = 1
res_sum = 0
for el in a:
    res_mul *= int(el)
    res_sum += int(el)
print(f'Произведение цифр = {res_mul}')
print(f'Сумма цифр = {res_sum}')
