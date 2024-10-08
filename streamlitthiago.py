import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import streamlit as st

st.title('DASHBOARD DE RECLAMAÇÕES NO RECLAME AQUI')


empresa = st.selectbox('SELECIONE A EMPRESA',
                        ['','Hapvida','Ibyte', 'Nagem'])

# Carregar o arquivo CSV
file_hapvida = pd.read_csv(r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\HAPVIDA_ETL.csv')
file_nagem = pd.read_csv(r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\NAGEM_ETL.csv')
file_ibyte = pd.read_csv(r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\IBYTE_ETL.csv')

status = st.selectbox('SELECIONE O STATUS',
                    ['Não respondida', 'Respondida',
                    'Resolvido', 'Em réplica','Não resolvido'],
                    index = 0)

col1, col2 = st.columns(2)

def total_reclamacoes(file):
    return file['STATUS'].value_counts().sum()

with col1:
    total = total_reclamacoes(file_hapvida) + total_reclamacoes(file_ibyte) + total_reclamacoes(file_nagem)
    st.metric(label='TOTAL RECLAMAÇÕES', value=f"{total:,}")

with col2:
    if (status in file_hapvida['STATUS'].value_counts() and
        status in file_ibyte['STATUS'].value_counts() and
        status in file_nagem['STATUS'].value_counts()):
        temp = (file_hapvida['STATUS'].value_counts().loc[status] +
                file_ibyte['STATUS'].value_counts().loc[status] +
                file_nagem['STATUS'].value_counts().loc[status])
    else:
        temp = 0  # Ou algum valor padrão

    st.metric(label=status.upper(), value=temp)

st.markdown('---')

#### Series temporais Número de Reclamações

