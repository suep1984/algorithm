lst = [num for num in range(2, 100)]
i = 2
count = 0
while 2 <= i <= 99:
    for num in lst:
        if num % i == 0:
            count += 1
    print(f'Чисел кратных {i} в диапазоне от 2 до 99 - {count}')
    count = 0
    i += 1
