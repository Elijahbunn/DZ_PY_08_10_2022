X1 = float(input(('Введите координаты первой точки на оси Х: ')))
Y1 = float(input(('Введите координаты первой точки на оси Y: ')))
X2 = float(input(('Введите координаты второй точки на оси Х: ')))
Y2 = float(input(('Введите координаты второй точки на оси Y: ')))

DeepX = (X2 - X1) ** 2
DeepY = (Y2 - Y1) ** 2

sum = DeepX + DeepY

import math
sqrt = round(math.sqrt(sum),2)

print(f'Расстояние между точками равно {sqrt}')