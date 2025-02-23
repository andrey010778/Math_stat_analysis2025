import numpy as np

X = [12.1, 14.7, 20.5, 16.6, 19]
Y = [53.2, 44.2, 51.4, 45.5, 34]
'''
Ручной расчёт коэффициента корреляции.
'''
n = len(X)
miu_x = sum(X) / n
miu_y = sum(Y) / n

stdev_x = (sum([(i - miu_x)**2 for i in X]) / n)**0.5
stdev_y = (sum([(i - miu_y)**2 for i in Y]) / n)**0.5

covariance = sum([(X[i] - miu_x) * (Y[i] -miu_y) for i in range(n)])
pearson_coefficient = covariance / (n * stdev_x * stdev_y)
print(round(pearson_coefficient, 3))
# 0.612
'''с помощью функции corrcoef() модуля numpy – возвращается массив, который содержит
искомый коэффициент для наблюдаемых величин.
'''
ar = np.array([X,Y], float)
c = np.corrcoef(ar)
print(c)
