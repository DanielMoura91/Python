import pandas as pd

df = pd.read_csv(r"data/ClientesBanco.csv",encoding='latin1')
df = df.drop("CLIENTNUM",axis=1)
display(df)
