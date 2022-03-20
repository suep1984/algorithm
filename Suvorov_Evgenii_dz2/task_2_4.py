n = int(input('Введите длину ряда: '))
delta = -1.5
elem = 1
result = 0
i = 1
while i <= n:
    result += elem
    elem += delta
    delta /= -2
    i += 1
print(result)
