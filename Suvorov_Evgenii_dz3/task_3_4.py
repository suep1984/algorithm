list1 = [2, 4, 54, 23, 65, 2, 43, 54, 3, 3, 3, 6, 7, 43]
element = 0
count = 0
for el in list1:
    if list1.count(el) > count:
        element = el
        count = list1.count(el)
        
print(element)
