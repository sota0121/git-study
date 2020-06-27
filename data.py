import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
print(df)
df.to_csv('log.csv')

