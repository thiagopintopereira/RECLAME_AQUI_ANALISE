import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import streamlit as st

# Carregar o arquivo CSV
file_hapvida = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_HAPVIDA.csv'
file_nagem = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_NAGEM.csv'
file_ibyte = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_IBYTE.csv'

# Tentar carregar o arquivo CSV
try:
    df = pd.read_csv(file_hapvida)
    st.success("Dados carregados com sucesso.")
except FileNotFoundError:
    st.error("Erro: O arquivo não foi encontrado. Verifique o caminho.")
except pd.errors.EmptyDataError:
    st.error("Erro: O arquivo está vazio.")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")

# Exibir as primeiras 30 linhas do DataFrame
st.write("Primeiras 30 linhas do DataFrame:")
st.dataframe(df.head(30))

# Converter a coluna 'TEMPO' para datetime
df['TEMPO'] = pd.to_datetime(df['TEMPO'])

# Plotar o número único de IDs por TEMPO
st.subheader('Número Único de IDs por Tempo')
fig1, ax1 = plt.subplots()
df.groupby('TEMPO').nunique()['ID'].plot(ax=ax1)
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Número de IDs')
st.pyplot(fig1)

# Contar valores únicos na coluna 'STATUS'
status_counts = df['STATUS'].value_counts()
st.write("Contagem de STATUS:")
st.bar_chart(status_counts)

# Extrair e manipular a coluna 'LOCAL'
estado_lista = df['LOCAL'].apply(lambda x: x.split('-', 2)[1].strip()).tolist()
df['ESTADO'] = estado_lista

# Plotar o número único de IDs por TEMPO para o estado 'CE'
st.subheader('Número de IDs por Tempo para CE')
fig2, ax2 = plt.subplots()
df[df['ESTADO'] == 'CE'].groupby('TEMPO').nunique()['ID'].plot(kind='bar', ax=ax2)
ax2.set_xlabel('Tempo')
ax2.set_ylabel('Número de IDs')
st.pyplot(fig2)

# Função para contar palavras em um texto
def count_palavras(texto):
    return len(texto.split())

# Plotar o histograma da contagem de palavras na coluna 'DESCRICAO'
st.subheader('Distribuição da Contagem de Palavras na Descrição')
fig3, ax3 = plt.subplots()
df['DESCRICAO'].apply(count_palavras).plot(kind='hist', density=True, ax=ax3)
ax3.set_xlabel('Número de Palavras')
ax3.set_ylabel('Densidade')
st.pyplot(fig3)

# Plotar a densidade da contagem de palavras na coluna 'DESCRICAO'
st.subheader('Densidade da Contagem de Palavras na Descrição')
fig4, ax4 = plt.subplots()
df['DESCRICAO'].apply(count_palavras).plot.kde(ax=ax4)
ax4.set_xlabel('Número de Palavras')
ax4.set_ylabel('Densidade')
st.pyplot(fig4)
