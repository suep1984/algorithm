list1 = [-2, -23, -5, -98, -4, 123]
list2 = [el for el in list1 if el < 0]

print(max(list2), '-', list2.index(max(list2)))

