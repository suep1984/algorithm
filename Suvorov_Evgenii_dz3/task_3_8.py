matrix = []
i = 0
print('Введите числа матрицы: ')
while i < 4:
    matrix.append([])
    j = 0
    while j < 4:
        matrix[i].append(input(f'{i + 1}:{j + 1}: '))
        j += 1
    i += 1

for string in matrix:
    string.append(str(sum(map(int, string))))
    print(f'|{"    ".join(string)}|')
