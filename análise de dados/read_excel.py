import pandas as pd

df = pd.read_excel('Vendas.xlsx') #ler tabela do excel

display(df) #Exibir tabela

lojas = df["ID Loja"].unique() #Cria uma lista de lojas com valores distintos

for loja in lojas:
  tabela_loja = df.loc[df["ID Loja"] == loja, ["ID Loja", "Quantidade", "Valor Final"]]
  tabela_loja = tabela_loja.groupby("ID Loja").sum()
  tabela_loja["Ticket Medio"] = tabela_loja["Valor Final"] / tabela_loja["Quantidade"]
  display(tabela_loja)
