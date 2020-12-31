import pandas as pd

df = pd.DataFrame(
    {
        "Nome": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Idade": [22, 35, 58],
        "Sexo": ["M", "M", "F"],
    }
)

nomes = df["Nome"]
idades = df["Idade"]
sexo = df["Sexo"]

print(df)
print(idades.describe())
