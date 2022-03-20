res_num = 0
res_sum = 0
while True:
    num = input('Введите натуральное число: ')
    if num == 'x':
        break
    _res = 0
    i = 0
    while i < len(num):
        _res += int(num[i])
        i += 1
    if _res > res_sum:
        res_sum = _res
        res_num = int(num)
print(res_num, res_sum)
