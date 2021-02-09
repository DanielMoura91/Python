import pandas as pd

df = pd.read_excel('data/Vendas.xlsx') 

display(df) 

df_fat = df[['ID Loja','Valor Final']].groupby('ID Loja').sum()
df_fat = df_fat.sort_values(by="Valor Final", ascending=False)  
display(df_fat)

df_qnt = df[['ID Loja','Quantidade']].groupby('ID Loja').sum()
df_qnt = df_qnt.sort_values(by="Quantidade", ascending=False)  
display(df_qnt)

tm = (df_fat['Valor Final'] / df_qnt['Quantidade']).to_frame()
tm = tm.rename(columns={0: 'Ticket Médio'})
display(tm)

table_complete = df_fat.join(df_qnt).join(tm)
display(table_complete)

def enviar_email(nome_da_loja, tabela):
  import smtplib
  import email.message

  server = smtplib.SMTP('smtp.gmail.com:587')  
  corpo_email = f"""
  <p>Prezados,</p>
  <p>Segue relatório de vendas</p>
  {tabela.to_html()}
  <p>Qualquer dúvida estou a disposição</p>
  """
    
  msg = email.message.Message()
  msg['Subject'] = f"Relatório de vendas - {nome_da_loja}"
    
  # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
  # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
  # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
  # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
  msg['From'] = 'seu_email'
  msg['To'] = 'email_do_destinatario'
  password = 'sua_senha'
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_email )
    
  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print('Email enviado')
 
lojas = df["ID Loja"].unique()

for loja in lojas:
  tabela_loja = df.loc[df["ID Loja"] == loja, ["ID Loja", "Quantidade", "Valor Final"]]
  tabela_loja = tabela_loja.groupby("ID Loja").sum()
  tabela_loja["Ticket Medio"] = tabela_loja["Valor Final"] / tabela_loja["Quantidade"]  
  enviar_email(loja,tabela_loja)
