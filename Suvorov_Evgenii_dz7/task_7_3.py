from random import randint

m = 3
array = [randint(0, 50) for el in range(2 * m + 1)]
print(array)
for i in range(m + 1):
    if i == m:
        print(array.pop(array.index(max(array))))
    else:
        array.pop(array.index(max(array)))
