import pandas as pd

df = pd.read_csv('file.csv')

df.to_csv('file.csv', index=False)
