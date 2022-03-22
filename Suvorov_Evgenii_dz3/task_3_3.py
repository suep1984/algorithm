from random import randint
list1 = [randint(0, 100) for i in range(0, 20)]
print(list1)
max_elem = max(list1)
max_elem_idx = list1.index(max_elem)
min_elem = min(list1)
min_elem_idx = list1.index(min_elem)
list1[max_elem_idx] = min_elem
list1[min_elem_idx] = max_elem
print(list1)
