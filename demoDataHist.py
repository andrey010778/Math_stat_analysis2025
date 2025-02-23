# import random
# import matplotlib.pyplot as plt
#
# k = 25
# '''
# random_numbers = [random.randint(0,100) for _ in range(1000)]
# '''
# mu = 0
# sigma = 1
# random_numbers = [random.normalvariate(mu, sigma) for _ in range(1000)]
# '''
#
# lambd = 0.5
# random_numbers = [random.expovariate(lambd) for _ in range(1000)]
# '''
#
# plt.hist(random_numbers, bins=k, density=True)
# plt.title("Histogram of normal distribution")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

'''Задание. 
Постройте гистограмму случайных чисел, полученных как сумма 12-ти случайных чисел, 
распределенных по равномерному закону распределения.
Сделайте вывод о предположительном виде закона распределения.
Посмотрите, как изменится график при суммировании двух, трех чисел.

'''
import random
import matplotlib.pyplot as plt

random_numbers =  [sum(random.randint(1,100) for val in range(12)) for val in range(1000)]

plt.hist(random_numbers, bins=10, density=True)
plt.title("Histogram of distribution")
plt.xlabel("Value")
plt.ylabel("Freqency")
plt.show()

# Предположительный вид закона распределения - нормальное распределение