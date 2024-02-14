import pandas as pd

data = pd.read_csv("1 - 1.csv")
prefix = "Т"
date = "19 Сентябрь 2017  17:13"
result = data[data.get("Фамилия", "").str.startswith(prefix) & (data.get("Завершено", "") < date)]
print(len(result))
print(result)
