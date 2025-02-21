# # Исходная выборка
# data = [12, 2, 6, 2, 6, 12, 6, 2, 6, 12, 6, 6, 12, 12, 12, 6, 6, 12, 6, 6]
#
# # 1. Составляем вариационный ряд (упорядочиваем по возрастанию)
# variational_series = sorted(data)
# print("Вариационный ряд:", variational_series)
#
# # 2. Составляем статистическое распределение (частота каждого уникального значения)
# frequency_distribution = {}
# for value in variational_series:
#     if value in frequency_distribution:
#         frequency_distribution[value] += 1
#     else:
#         frequency_distribution[value] = 1
#
# print(frequency_distribution)

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Исходные данные
# data1 = [7.5, 6.1, 7, 6, 7.4, 6.8, 6.3, 7.5, 7, 7.5, 7.6, 10.6, 6, 8.2, 7.1, 9.6, 8.5, 9.2, 8, 8, 8.7, 9.8, 8.3, 8.5, 9.5, 6.3, 5.8, 7.2, 7.5, 6.5]
#
# # 1. Вариационный ряд
# variational_series = sorted(data1)
# print("Вариационный ряд:", variational_series)
#
# # 2. Гистограмма и полигон относительных частот
#
# # Определяем количество интервалов по формуле Стерджеса
# n = len(data1)
# k = int(1 + 3.322 * np.log10(n))  # Формула Стерджеса
# print("Количество интервалов:", k)
#
# # Строим гистограмму
# plt.figure(figsize=(10, 6))
# counts, bins, patches = plt.hist(data1, bins=k, edgecolor='black', alpha=0.7, density=True, label='Гистограмма')
#
# # Добавляем полигон относительных частот
# midpoints = 0.5 * (bins[1:] + bins[:-1])  # Середины интервалов
# plt.plot(midpoints, counts, 'ro-', label='Полигон частот')
#
# # Настройка графика
# plt.title('Гистограмма и полигон относительных частот')
# plt.xlabel('Значения')
# plt.ylabel('Относительная частота')
# plt.legend()
# plt.grid(True)
# plt.show()

import random
import matplotlib.pyplot as plt

random_numbers =  [sum(random.randint(1,100) for val in range(3)) for val in range(1000)]

plt.hist(random_numbers, bins=10, density=True)
plt.title("Histogram of distribution")
plt.xlabel("Value")
plt.ylabel("Freqency")
plt.show()

