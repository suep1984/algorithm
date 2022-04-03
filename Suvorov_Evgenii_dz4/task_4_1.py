import timeit as tm


code = """matrix = [
     [1231, 312, 12, 123, 4487],
     [12, 12, 12, 12, 48],
     [213, 2, 123, 123, 461],
     [12, 312, 312, 21, 657]
 ]
min_elements = []
i = 0
while i < len(matrix[0]):
    j = 0
    _res = []
    while j < len(matrix):
        _res.append(matrix[j][i])
        j += 1
    min_elements.append(min(_res))
    i += 1"""
time = tm.timeit(code, number=100) / 100

print(time)

# Сложность алгоритма - O(n^2) jп тому как присутствует вложенный цикл и, сделовательно, дополнительный перебор элементов
