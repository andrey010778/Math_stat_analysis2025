import statistics

year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]
slope, intercept = statistics.linear_regression(year, films_total)
print(round(slope*2019+intercept))