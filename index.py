import streamlit as st
import pandas as pd

# Titulo do site
st.set_page_config(page_title="TSI - Canguaretama")

# Main
st.title('Curso: Tecnologia em Sistemas para Internet - TSI') 

# Sidebar turmas
st.sidebar.title('Menu do Curso: Tecnologia em Sistemas para Internet - TSI')
turma = st.sidebar.selectbox('Selecione uma turma', ['TSI - 2020', 'TSI - 2021', 'TSI - 2022', 'TSI - 2023'])
    
if turma == 'TSI - 2020':
    st.write("---")
    st.title('Turma: TSI - 2020')
    st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif turma == 'TSI - 2021':
    st.title('Turma: TSI - 2021')
    st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif turma == 'TSI - 2022':
    st.title('Turma: TSI - 2022')
    st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif turma == 'TSI - 2023':
    st.title('Turma: TSI - 2023')
    st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])


# Sidebar período
periodo = st.sidebar.selectbox('Selecione um período', ['Período 1º', 'Período 2º', 'Período 3º', 'Período 4º', 'Período 5º', 'Período 6º'])
    
if periodo == 'Período 1º':
    st.write("---")
    st.title('Periodo: 1º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif periodo == 'Período 2º':
    st.title('Periodo: 2º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif periodo == 'Período 3º':
    st.title('Periodo: 3º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif periodo == 'Período 4º':
    st.title('Periodo: 4º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif periodo == 'Período 5º':
    st.title('Periodo: 5º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])

elif periodo == 'Período 6º':
    st.title('Periodo: 6º')
    # st.selectbox('Selecione um período', ['1º Período', '2º Período', '3º Período', '4º Período', '5º Período', '6º Período'])


    
# x = st.slider('x') # 👈~this is a widget 
# st.write(x, 'squared is', x * x)    