import pandas as pd
import numpy as np

data = pd.read_csv("youtube.csv")

result = data.head(10)
result = data[10:15]

result = data.columns
result = len(data.columns) 

result = data.drop("Name", axis=1)

result = data[:50][["Category","Country"]]
print(result)
result = data.loc[data["Subscribers (millions)"] == data["Subscribers (millions)"].max(),["Name"]]
result = data["Subscribers (millions)"].mean()
result = data.loc[data["Subscribers (millions)"] == data["Subscribers (millions)"].min(),["Name"]]
result = data.head(10)["Subscribers (millions)"].max()


