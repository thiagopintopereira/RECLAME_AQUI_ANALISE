import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Carregar o arquivo CSV
file_hapvida = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_HAPVIDA.csv'

# Tentar carregar o arquivo CSV
try:
    df = pd.read_csv(file_hapvida)
    st.success("Dados carregados com sucesso.")
except FileNotFoundError:
    st.error("Erro: O arquivo não foi encontrado. Verifique o caminho.")
    df = pd.DataFrame()  # Definindo df como um DataFrame vazio
except pd.errors.EmptyDataError:
    st.error("Erro: O arquivo está vazio.")
    df = pd.DataFrame()  # Definindo df como um DataFrame vazio
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    df = pd.DataFrame()  # Definindo df como um DataFrame vazio


    # Converter a coluna 'TEMPO' para datetime
    df['TEMPO'] = pd.to_datetime(df['TEMPO'])

    # Plotar o número único de IDs por TEMPO
st.subheader('Número Único de IDs por Tempo')

# Criar uma figura e um eixo
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Agrupar por 'TEMPO' e contar IDs únicos
df.groupby('TEMPO').nunique()['ID'].plot(ax=ax1)

# Configurar os rótulos dos eixos
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Número de IDs')
ax1.set_title('Contagem de IDs Únicos por Tempo')

# Exibir o gráfico no Streamlit
st.pyplot(fig1)
