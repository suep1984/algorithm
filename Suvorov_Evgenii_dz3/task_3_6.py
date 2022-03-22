list1 = [2, -23, 5, 98, 400, 123]
if list1.index(min(list1)) < list1.index(max(list1)):
    res = len(list1[list1.index(min(list1)) + 1:list1.index(max(list1))])
else:
    res = len(list1[list1.index(max(list1)) + 1:list1.index(min(list1))])
print(res)
