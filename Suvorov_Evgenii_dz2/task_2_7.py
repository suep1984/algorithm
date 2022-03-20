def get_progression(n):
    if n == 1:
        return n
    return get_progression(n - 1) + n


n = int(input('Введите "n": '))
print(get_progression(n) == n * (n + 1) / 2)
