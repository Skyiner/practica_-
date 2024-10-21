import math
from math import *
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))
if x + pow(fabs(y), 1./4) > 0:
    a1 = pow((9 + (x - y) ** 2), 1 / 3) / (x ** 2 + y ** 2 + 2)
    a2 = exp(fabs(x-y))
    a3 = tan(z)**3
    s=a1-a2*a3
    print("Результат ", s)
else:
    print("Значение выражения не может быть вычислено")
