import pandas as pd

df = pd.read_csv("data/exoplanetas.csv", comment="#")
print(df.shape)
print(df.head())
print(df.isna().sum())