sequence = input('Введите последовательность чисел: ')
element = input('введите искомую цифру: ')

count = 0
for el in sequence:
    if element == el:
        count += 1

print(count)
