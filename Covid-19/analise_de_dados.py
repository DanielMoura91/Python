import pandas as pd

confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
recoveries_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

'''
print(confirmed_df.head(10))
print(deaths_df.head(10))
print(recoveries_df.head(10))
'''

date = '3/10/21' # Data no padrão m/d/aa

df_confirmed = pd.DataFrame(confirmed_df[["Country/Region",date]].groupby("Country/Region").sum())
df_confirmed = df_confirmed.sort_values(by=date,ascending=False)
df_confirmed.columns = ['Confirmados']
table1 = df_confirmed.head(10)
print(table1)

df_deaths = pd.DataFrame(deaths_df[["Country/Region",date]].groupby("Country/Region").sum())
df_deaths = df_deaths.sort_values(by=date,ascending=False)
df_deaths.columns = ['Mortes']
table2 = df_deaths.head(10)
print(table2)

df_recoveries = pd.DataFrame(recoveries_df[["Country/Region",date]].groupby("Country/Region").sum())
df_recoveries = df_recoveries.sort_values(by=date,ascending=False)
df_recoveries.columns = ['Recuperados']
table3 = df_recoveries.head(10)
print(table3)

tl = ((df_deaths['Mortes'] / df_confirmed['Confirmados'])*100).to_frame()
tl = tl.rename(columns={0: 'Taxa Let'})

result = pd.concat([df_confirmed, df_deaths, df_recoveries], axis=1, join="inner").join(tl)
table4 = result.head(10)
print(table4)

table5 = result.head(10).describe()
print(table5)
