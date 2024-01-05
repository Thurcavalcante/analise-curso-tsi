# Importando bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', page_title='Dashboard 1')

# Leitura de dados
df = pd.read_csv('alunos.csv')

st.title('Perfil dos Alunos do Curso de Tecnologia em Sistemas para Internet - TSI')

st.header('Dashboard - Alunos')

# Função que constroe gráfico em barras
def constroi_grafico_barras(variavel):
    contagem = df[variavel].value_counts().reset_index()
    fig = px.bar(contagem, x=variavel, y='count', title='Quantidade de Alunos por ' + variavel, text_auto=True)
    return fig

col1, col2, col3 = st.columns(3)

grafico1 = constroi_grafico_barras('Turma')
col1.plotly_chart(grafico1)

grafico2 = constroi_grafico_barras('Cidade')
col2.plotly_chart(grafico2)

grafico3 = constroi_grafico_barras('A regiao em que mora')
col3.plotly_chart(grafico3)