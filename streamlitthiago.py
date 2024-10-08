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

col1 , col2 = st.columns(2)
with col1:
    total = file_hapvida['STATUS'].value_counts().sum() + file_ibyte['STATUS'].value_counts().sum() + file_nagem.value_counts().sum()
    st.metric(label='TOTAL RECLAMAÇÕES',
            value=total)
with col2:
    temp = file_hapvida['STATUS'].value_counts().loc[status] + file_ibyte['STATUS'].value_counts().loc[status] + file_nagem['STATUS'].value_counts().loc[status]
    st.metric(label= status.upper(),
              value=temp)

st.markdown('---')

#### Series temporais Número de Reclamações

