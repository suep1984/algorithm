from random import randint

array = [randint(-100, 100) for i in range(20)]
print(array)
for i in range(len(array)):
    for j in range(len(array) - 1 - i):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
