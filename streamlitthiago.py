import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import streamlit as st
import os

st.title('DASHBOARD DO RECLAME AQUI')

# Seleção da empresa
empresa = st.sidebar.selectbox('SELECIONE A EMPRESA', ['Hapvida', 'Ibyte', 'Nagem'])

# Dicionário de imagens
images = {
    'Hapvida': 'hapvida.png',
    'Nagem': 'nagem.png',
    'Ibyte': 'ibyte.png'
}

# Exibir a imagem correspondente na sidebar
if empresa:
    image_file = images.get(empresa)
    if image_file and os.path.isfile(image_file):
        st.sidebar.image(image_file, use_column_width=True)
    else:
        st.sidebar.error(f"Imagem não encontrada: {image_file}")


# Carregar os arquivos CSV
file_hapvida = pd.read_csv('HAPVIDA_ETL.csv')
file_nagem = pd.read_csv('NAGEM_ETL.csv')
file_ibyte = pd.read_csv('IBYTE_ETL.csv')

# Dicionário para armazenar os DataFrames
dfs = {
    'Hapvida': file_hapvida,
    'Ibyte': file_ibyte,
    'Nagem': file_nagem
}

status = st.selectbox('SELECIONE O STATUS',
                       ['Não respondida', 'Respondida',
                        'Resolvido', 'Em réplica', 'Não resolvido'],
                       index=0)

# Calcular o total de reclamações
total = sum(df['STATUS'].value_counts().sum() for df in dfs.values())
st.metric(label='TOTAL RECLAMAÇÕES', value=total)

# Calcular o total de reclamações pelo status selecionado
temp = sum(df['STATUS'].value_counts().get(status, 0) for df in dfs.values())
st.metric(label=status.upper(), value=temp)

st.markdown('---')

# Gráfico de reclamações ao longo do tempo

st.header(f'Reclamações ao longo do tempo - {empresa}')
if empresa:
    df = dfs[empresa]
    df['TEMPO'] = pd.to_datetime(df['TEMPO'])  # Converter para datetime

  

   # Agrupar as reclamações por data
reclamacoes_por_data = df.groupby(df['TEMPO'].dt.date)['DESCRICAO'].count()

# Criar o gráfico de reclamações ao longo do tempo
plt.figure(figsize=(10, 5))
plt.plot(reclamacoes_por_data.index, reclamacoes_por_data.values, marker='o')
plt.title(f'Reclamações ao Longo do Tempo - {empresa}')
plt.xlabel('Data')
plt.ylabel('Número de Reclamações')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Mostrar o gráfico no Streamlit
st.pyplot(plt)


st.header(f'Reclamações por Estado - {empresa}')
# Agrupar as reclamações por estado
reclamacoes_por_estado = df.groupby('ESTADO')['DESCRICAO'].count()
# Ordenar do maior para o menor
reclamacoes_por_estado = reclamacoes_por_estado.sort_values(ascending=False)

# Criar o gráfico de reclamações por estado
plt.figure(figsize=(10, 5))
plt.bar(reclamacoes_por_estado.index, reclamacoes_por_estado.values, color='blue')
plt.title(f'Reclamações por Estado - {empresa}')
plt.xlabel('Estado')
plt.ylabel('Número de Reclamações')
plt.xticks(rotation=45)
plt.grid(axis='y')  # Grade apenas nas linhas horizontais
plt.tight_layout()

# Mostrar o gráfico no Streamlit
st.pyplot(plt)
