# Importa as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(layout="wide", page_title="Page 4")

# Carregar dados do arquivo CSV para um DataFrame
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",") 

# Converter a coluna "Date" para o tipo de dados datetime e ordenar o DataFrame por data
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criar uma nova coluna "Month" que representa o ano e o mês da venda
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma barra lateral interativa para selecionar o mês desejado
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Filtrar o DataFrame para mostrar apenas dados do mês selecionado
df_filtered = df[df["Month"] == month]

# Criar colunas para layout da página (2 colunas, 3 colunas, 3 colunas)
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Criar gráfico de barras para o faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Criar gráfico de barras para o faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Calcular o faturamento total por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()

# Criar gráfico de barras para o faturamento por filial
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Criar gráfico de pizza para o faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Calcular a média de avaliação por filial
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()

# Criar gráfico de barras para a avaliação por filial
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)