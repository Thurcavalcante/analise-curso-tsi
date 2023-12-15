"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd
import time

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# 
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Este exemplo usa Numpy para gerar uma amostra aleatória, 
# mas você pode usar Pandas DataFrames, matrizes Numpy ou 
# matrizes Python simples.
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# Vamos expandir o primeiro exemplo usando o objeto Pandas 
# Styler para destacar alguns elementos da tabela interativa.
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# Streamlit também possui um método para geração de tabelas 
# estáticas: st.table().
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

# Desenhe um gráfico de linhas: Você pode adicionar facilmente 
# um gráfico de linhas ao seu aplicativo com st.line_chart(). 
# Iremos gerar um aleatório amostra usando Numpy e, em seguida, 
# faça um gráfico.
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Trace um mapa: Com st.map() você pode exibir pontos de dados 
# em um mapa. Vamos usar o Numpy para gerar alguns dados de 
# amostra e plotá-los em um mapa de São Francisco.
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Widgets: Quando você coloca os dados ou o modelo no estado 
# que deseja explorar, você pode adicionar widgets como 
# st.slider(), st.button() ou st.selectbox(). É muito simples
# — trate os widgets como variáveis:
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Os widgets também podem ser acessados ​​por chave, se você 
# optar por especificar uma string para usar como chave 
# exclusiva do widget:
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# Use caixas de seleção para mostrar/ocultar dados: 
# Um caso de uso das caixas de seleção é ocultar ou mostrar um 
# gráfico ou seção específica em um aplicativo. st.checkbox()
# recebe um único argumento, que é o rótulo do widget. 
# Neste exemplo, a caixa de seleção é usada para alternar um 
# declaração condicional.
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
# Use uma caixa de seleção para opções: Use st.selectbox para 
# escolher uma série. Você pode escrever as opções desejadas 
# ou passar por um array ou quadro de dados coluna.
# Vamos usar o df quadro de dados que criamos anteriormente.
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# O Streamlit facilita a organização de seus widgets em uma barra 
# lateral do painel esquerdo com st.sidebar. Cada elemento passado 
# para st.sidebar é fixado à esquerda, permitindo os usuários se 
# concentrem no conteúdo do seu aplicativo e ainda tenham acesso à 
# IU controles.
# Por exemplo, se você quiser adicionar uma caixa de seleção e um 
# controle deslizante a uma barra lateral, use st.sidebar.slider e 
# st.sidebar.selectbox em vez de st.slider e st.selectbox:

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Além da barra lateral, o Streamlit oferece diversas outras maneiras 
# de controlar o layout do seu aplicativo. st.columns permite colocar 
# widgets lado a lado e st.expander permite economizar espaço ocultando 
# conteúdo grande.
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
# Mostrar progresso: Ao adicionar cálculos de longa duração a um 
# aplicativo, você pode usar st.progress() para exibir o status em 
# tempo real. Primeiro, vamos importar o tempo. Usaremos o método 
# time.sleep() para simular um cálculo de longa duração: 

# import time

# Agora, vamos criar uma barra de progresso:

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

# Temas
# Streamlit oferece suporte a temas claros e escuros prontos para 
# uso. Streamlit irá primeiro verifique se o usuário que visualiza 
# um aplicativo tem uma preferência de modo Claro ou Escuro definida 
# por seu sistema operacional e navegador. Se sim, então essa preferência 
# será usada. Caso contrário, o tema Claro será aplicado por padrão.

# Você também pode alterar o tema ativo de "⋮" → "Configurações".

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")