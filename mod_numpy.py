import numpy as np

data = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
data1 = data + 2
print(data1)
print(type(data))
print(data.nbytes)
data = data.astype('int64')
print(data.dtype)

array2d = np.array([[0.0, 0.1, 0.2], [1.0, 1.1, 1.2], [2.0, 2.1, 2.2]])
print(array2d)
print(array2d[1, 1])
print(array2d[2:, :])
array2d[2:, :] = array2d[2:, :] * 2
print(array2d)

print(array2d[:, 1:2])

names = np.array(['Sergey', 'Ivan', 'Ivan', 'Sergey', 'Alexey', 'Dmitrij', 'Pavel'])
print(names == 'Sergey')

numbers = np.array([1, 2, 3, 4, 5, 6, 7])
print(numbers[names == 'Sergey'])

mask = (names == 'Sergey') | (names == 'Ivan')
print(mask)
print(numbers[mask])
print(numbers[~mask])

arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
print(arr[indices])

indices = np.array([4, 0, 0])
print(arr[indices])

arr_2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                 [7, 8, 9]])
row_indices = np.array([0, 2])
col_indices = np.array([1,2])

print(arr_2d[row_indices, col_indices])

data = np.array([1, 2, 2, 2, 3, 4, 4, 4, 1])
print(np.mean(data)) #среднее значение
print(np.median(data)) #медиана
print(np.min(data))
print(np.max(data))
print(np.sum(data))
print(np.argmax(data))
print(np.argmin(data))
print(np.std(data)) #стандартное отклонение
print(np.var(data)) #дисперсия

matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                  [7, 8, 9]])
print(np.sum(matrix, axis=0))
print(np.mean(matrix, axis=1))
print(np.max(matrix))

data = np.array([10, 20, 30, 40, 50])
print(np.percentile(data, 25))
print(np.percentile(data, 50))
print(np.percentile(data, 90))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
print(np.corrcoef(x, y))
print(np.cov(x, y))

marks = np.array([5.0, 4.0, 5.0, 3.0, 5.0])
weights = np.array([1.0, 1.5, 1.0, 2.0, 1.0])
weighted_avg=np.average(marks, weights=weights)
print("Средневзвешенное:", weighted_avg)

data = np.array([2, 2, 3, 5, 5, 5])
unique, counts = np.unique(data, return_counts=True)
print('Unique:', unique) #Уникальные
print('Count', counts) #Частоты

data = np.array([1, 2, 3, 4, 5, 6])
print(np.cumsum(data))

'''Hometask:'''

goals = []

for i in range(7):
    i = int(input('Input score: '))
    goals.append(i)

hard_coef = float(input('Input hard coef from 1.2 to 3.6: '))

def trim_mean_dive(goals, hard_coef):
    sorted_array = sorted(goals)
    cut_middle = sorted_array[1:-1]
    final_score = sum(cut_middle)*hard_coef
    return final_score

trim_mean_dive(goals, hard_coef)
