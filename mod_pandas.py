import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import kagglehub

series = pd.Series([10, 20,30, 40, 50])
print(series)
print(series.values)
print(series.index)

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
print(df)

df = pd.DataFrame({'A': [1, 4],
                   'B': [2, 5],
                   'C': [3, 6]})

#path = kagglehub.read_csv()
data = pd.Series([0, np.nan, 100])
print(data.mean())

x = [1, 2, 3, 4, 5]
y = [10, 20, np.nan, 40, 50]

plt.plot(x, y, marker='o', color='red', linestyle='--')
plt.title('Graph with missing data')
#plt.show()

#titanic = pd.read_csv("https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv")
#titanic.head()

