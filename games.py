import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/vitisg/vendasdegames/main/vgsales.csv")

df = df.dropna()

df['Year'] = df['Year'].astype(int)

df = df.rename(columns = {'Name': 'Nome', 'Platform': 'Plataforma', 'Year': 'Ano de lançamento', 'Genre': 'Genêro', 'Publisher': 'Publicadora', 'NA_Sales': 'Vendas na américa do sul',
       'EU_Sales': 'Vendas nos EUA', 'JP_Sales': 'Vendas no Japão', 'Other_Sales': 'Vendas em outros lugares', 'Global_Sales': 'Venda global'})



sns.countplot(df['Genêro'])
fig = plt.gcf()
fig.set_size_inches(15,10)
plt.title('Type')

