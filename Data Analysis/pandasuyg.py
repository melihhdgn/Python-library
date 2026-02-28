import pandas as pd
import numpy as np

data = pd.read_csv("world_economics.csv")
#result = data.head(10)
#result = len(data.index)
#result = data["Interest Rate"].mean()
#result1 = data["Interest Rate"].max()
#result = data.loc[data["Interest Rate"] == result1,["name","Interest Rate"]] # en yüksek enflasyona sahip ülke ismi 
#result = data[(data["Interest Rate"] > 5) & (data["Interest Rate"] < 25)][["name", "capital"]] #enflasyona 5 25 arasında olanlar namesi ve capitalı
#result = data.loc[data["capital"] == "Amman",["name"]] #capitalı amman olan name yi yazır 
#result = data[data.name.str.contains("t")] # t olan nameleri yazdır 
print(result)


