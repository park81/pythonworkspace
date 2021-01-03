import pandas as pd 

data = pd.read_csv("merge.csv",encoding='CP949')

data2 = data.iloc[:,[0,1,2,15,16,17,18,19,20,21,22,3220,3221,3222,3223]]
#print(data2)


data2.to_csv("result.csv")


