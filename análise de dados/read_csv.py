import pandas as pd

#titanic = pd.read_csv("data/titanic.csv")

titanic = pd.read_csv(
    "https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv")

print(titanic.head())
