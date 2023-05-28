import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/vitisg/vendasdegames/main/vgsales.csv")

df = df.dropna()

df['Year'] = df['Year'].astype(int)

df = df.rename(columns = {'Name': 'Nome', 'Platform': 'Plataforma', 'Year': 'Ano de lançamento', 'Genre': 'Genêro', 'Publisher': 'Publicadora', 'NA_Sales': 'Vendas na américa do sul',
       'EU_Sales': 'Vendas nos EUA', 'JP_Sales': 'Vendas no Japão', 'Other_Sales': 'Vendas em outros lugares', 'Global_Sales': 'Venda global'})
st.title('DADOS DE VENDAS GLOBAL DE JOGOS DE VIDEOGAME')
st.write(
              'Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de local para mostrar as vendas por gênero no gráfico. Utilize o as abas abaixo para escolher o tipo de análise ')

tab1, tab2 = st.tabs(["Localidade", "Dog"])
with tab1:
       locais = ['Vendas na américa do sul', 'Vendas nos EUA',
                 'Vendas no Japão', 'Vendas em outros lugares', 'Venda global']
       local = st.selectbox('Qual o local das vendas?', locais)
       col1, col2 = st.columns(2)
       with col1:
              st.header("Análise das vendas por gênero e localidade")
              fig = px.histogram(df, x='Genêro', y=local)
              fig.update_layout(bargap=0.2)
              st.plotly_chart(fig, use_container_width=True)

       with col2:
              st.header("Análise das vendas por plataforma e localidade")
              fig = px.histogram(df, x='Plataforma', y=local, )
              fig.update_layout(yaxis_title=' ', bargap=0.2)
              st.plotly_chart(fig, use_container_width=True)
