from random import randint

list1 = [randint(1, 100) for elem in range(0, 20)]
list2 = []
i = 0
while i < len(list1):
    if list1[i] % 2 == 0:
        list2.append(i)
    i += 1

print(list2)
