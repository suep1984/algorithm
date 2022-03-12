import time

start_time = time.time()
lst_int = []
lst_flt = []
lst_smbl = []
a = 1
b = 100
c = 1,2
d = 444,22
e = 'f'
f = 'r'
for i in range(a, b + 1):
    lst_int.append(i)
shift = int(str(time.time() - start_time)[3:len(str(len(lst_int))) + 2])
print(lst_int[shift])
