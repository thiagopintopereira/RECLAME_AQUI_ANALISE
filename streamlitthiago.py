import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import streamlit as st
import os

st.title('DASHBOARD DO RECLAME AQUI')


# Carregar os arquivos CSV
file_hapvida = load_csv('HAPVIDA_ETL.csv')
file_nagem = load_csv('NAGEM_ETL.csv')
file_ibyte = load_csv('IBYTE_ETL.csv')

# Dicionário para armazenar os DataFrames
dfs = {
    'Hapvida': file_hapvida,
    'Ibyte': file_ibyte,
    'Nagem': file_nagem
}

# Dicionário de imagens
images = {
    'Hapvida': 'hapvida.png',
    'Nagem': 'nagem.png',
    'Ibyte': 'ibyte.png'
}

# Seleção da empresa
empresa = st.sidebar.selectbox('SELECIONE A EMPRESA', ['', 'Hapvida', 'Ibyte', 'Nagem'])

# Exibir a imagem correspondente
if empresa:
    image_file = images.get(empresa)
    image_path = os.path.join(directory_path, image_file)
    if os.path.isfile(image_path):
        st.image(image_path, caption=empresa, use_column_width=True)
    else:
        st.error(f"Imagem não encontrada: {image_path}")

    # Exibir informações do DataFrame correspondente
    df = dfs.get(empresa)
    if df is not None:
        st.write(df)

        # Cálculo do total de reclamações
        total = df['STATUS'].value_counts().sum()
        st.metric(label='TOTAL RECLAMAÇÕES', value=total)

        # Seleção do status
        status = st.selectbox('SELECIONE O STATUS',
                               ['Não respondida', 'Respondida', 'Resolvido', 'Em réplica', 'Não resolvido'],
                               index=0)

        # Calcular o total de reclamações pelo status selecionado
        temp = df['STATUS'].value_counts().get(status, 0)
        st.metric(label=status.upper(), value=temp)

        st.markdown('---')

        # Gráfico de reclamações ao longo do tempo
        st.header(f'Reclamações ao longo do tempo - {empresa}')
        df['TEMPO'] = pd.to_datetime(df['TEMPO'], errors='coerce')  # Converter para datetime

        # Agrupar as reclamações por data
        reclamacoes_por_data = df.groupby(df['TEMPO'].dt.date)['DESCRICAO'].count()

        # Criar o gráfico
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
    # Mostrar o gráfico no Streamlit
    st.pyplot(plt)
#### Series temporais Número de Reclamações

