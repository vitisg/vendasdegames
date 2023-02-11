import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/vitisg/vendasdegames/main/vgsales.csv")

df = df.dropna()

df['Year'] = df['Year'].astype(int)

df = df.rename(columns = {'Name': 'Nome', 'Platform': 'Plataforma', 'Year': 'Ano de lançamento', 'Genre': 'Genêro', 'Publisher': 'Publicadora', 'NA_Sales': 'Vendas na américa do sul',
       'EU_Sales': 'Vendas nos EUA', 'JP_Sales': 'Vendas no Japão', 'Other_Sales': 'Vendas em outros lugares', 'Global_Sales': 'Venda global'})

st.title('DADOS DE VENDAS GLOBAL DE JOGOS DE VIDEOGAME')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o grafico. Utilize o menu lateral para alterar a amostragem')
fig = px.histogram(df, x="Genêro")
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)
st.caption('Os dados foram obtidos a partir o site: https://www.kaggle.com/datasets/thedevastator/global-video-game-sales')


#ANALISE DE VENDAS
locais = ['Vendas na américa do sul', 'Vendas nos EUA',
       'Vendas no Japão', 'Vendas em outros lugares', 'Venda global']
local = st.sidebar.selectbox('Qual o local das vendas?', locais)

fig = px.histogram(df, x=local)
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)
