print("Введите координаты первой точки")
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print("Введите координаты второй точки")
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
if str(b)[0] == "-":
    print(f'Уравнение прямой: y = {k}x - {str(b)[1:]}')
else:
    print(f'Уравнение прямой: y = {k}x + {b}')
