import timeit as tm


code1 = """def get_prime_number(stop, i):
    prime_num = []
    for prime in range(2, stop + 1):
        is_prime = True
        for num in range(2, prime):
            if prime % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(prime)
    print(f'Prime number list: {prime_num}')
    return f'Requested number is {prime_num[i - 1]}'


print(get_prime_number(10010, 1))"""


code2 = """def get_prime_number_eratosfen(stop, idx):
    is_prime = [True for n in range(stop + 1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, stop + 1):
        if is_prime[i]:
            for j in range(2 * i, stop + 1, i):
                is_prime[j] = False
    prime_num = []
    for i in range(2, stop + 1):
        if is_prime[i]:
            prime_num.append(i)
    print(f'Prime number list: {prime_num}')
    return f'Requested number is {prime_num[idx - 1]}'


print(get_prime_number_eratosfen(10010, 1))"""

time_code1 = tm.timeit(code1, number=1)
time_code2 = tm.timeit(code2, number=1)
print(f'Execution time using the Eratosthenes algorithm is {time_code2}')
print(f'Execution time using another algorithm is {time_code1}')
#Время выполнения программы без использования алгоритма Эратосфена на 2 порядка выше чем с его использованием по причине большего перебора массива
