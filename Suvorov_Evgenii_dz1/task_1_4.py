import time
import numpy

start_time = time.time()
lst_int = []
lst_flt = []
lst_smbl = []
a = 1
b = 100
c = 1.2
d = 444.22
e = 'f'
f = 'r'
for i in range(a, b + 1):
    lst_int.append(i)
for i in numpy.arange(c, d, 0.1):
    lst_flt.append(i)
for i in range(ord(e), ord(f) + 1):
    lst_smbl.append(chr(i))
shift_int = int(str(time.time() - start_time)[3:len(str(len(lst_int))) + 2])
shift_flt = int(str(time.time() - start_time)[3:len(str(len(lst_flt))) + 2])
shift_smbl = int(str(time.time() - start_time)[3:len(str(len(lst_smbl))) + 2])
print(lst_int[shift_int])
print(lst_flt[shift_flt])
print(lst_smbl[shift_smbl])
print(str(time.time() - start_time)[6:8])
print(shift_int)
