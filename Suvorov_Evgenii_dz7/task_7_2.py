from random import randint


def merge_sort(a):
    lenght = len(a)
    if lenght < 2:
        return a
    left = merge_sort(a[:lenght // 2])
    right = merge_sort(a[lenght // 2:])
    i = 0
    j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append((left[i]))
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


array = [randint(0, 50) for i in range(20)]
print(array)
array = merge_sort(array)
print(array)
