import pandas as pd

print("Extract data from mysql")

data = {
    'id':[1,2,3],
    "name":['a','b','c']
}

df = pd.DataFrame(data)
print(df)
