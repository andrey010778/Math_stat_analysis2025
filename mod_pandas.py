import pandas as pd
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

path = kagglehub.read_csv()