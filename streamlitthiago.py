import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import streamlit as st

st.title('DASHBOARD ANÁLISE RECLAME AQUI')

# Carregar os arquivos CSV
file_hapvida = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\HAPVIDA_ETL.csv'
file_nagem = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\NAGEM_ETL.csv'
file_ibyte = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\IBYTE_ETL.csv'

# Ler os DataFrames
df_hapvida = pd.read_csv(file_hapvida)
df_nagem = pd.read_csv(file_nagem)
df_ibyte = pd.read_csv(file_ibyte)

# Seleção da empresa
empresa = st.selectbox('SELECIONE A EMPRESA', ['Hapvida', 'Ibyte', 'Nagem'])

# Seleção do status
status = st.selectbox('SELECIONE O STATUS', ['Não respondida', 'Respondida', 'Resolvido', 'Em réplica', 'Não resolvido'], index=0)

# Calcular total de reclamações
total = (
    df_hapvida['STATUS'].value_counts().sum() +
    df_ibyte['STATUS'].value_counts().sum() +
    df_nagem['STATUS'].value_counts().sum()
)

# Exibir total de reclamações
col1, col2 = st.columns(2)
with col1:
    st.metric(label='TOTAL RECLAMAÇÕES', value=total)

# Calcular e exibir o total para o status selecionado
with col2:
    temp_hapvida = df_hapvida['STATUS'].value_counts().get(status, 0)
    temp_nagem = df_nagem['STATUS'].value_counts().get(status, 0)
    temp_ibyte = df_ibyte['STATUS'].value_counts().get(status, 0)
    
    temp = temp_hapvida + temp_nagem + temp_ibyte
    st.metric(label=status.upper(), value=temp)

st.markdown('---')
