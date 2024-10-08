import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy

# Carregar o arquivo CSV
file_hapvida = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_HAPVIDA.csv'
file_nagem = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_NAGEM.csv'
file_ibyte = r'C:\Users\thiag\OneDrive\Área de Trabalho\Pyhton\RECLAMEAQUI_IBYTE.csv'



try:
    df = pd.read_csv(file_hapvida)
    print("Dados carregados com sucesso.")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o caminho.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio.")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")

# Exibir as primeiras 30 linhas do DataFrame
print(df.head(30))

# Converter a coluna 'TEMPO' para datetime
df['TEMPO'] = pd.to_datetime(df['TEMPO'])

# Plotar o número único de IDs por TEMPO
df.groupby('TEMPO').nunique()['ID'].plot(title='Número Único de IDs por Tempo')
plt.xlabel('Tempo')
plt.ylabel('Número de IDs')
plt.show()

# Contar valores únicos na coluna 'STATUS'
status_counts = df['STATUS'].value_counts()
print("Contagem de STATUS:")
print(status_counts)

# Extrair e manipular a coluna 'LOCAL'
primeiro_local = df['LOCAL'].iloc[0]
estado = primeiro_local[-2:]
print(f"Estado extraído: {estado}")

# Criar uma lista de estados a partir da coluna 'LOCAL'
estado_lista = df['LOCAL'].apply(lambda x: x.split('-', 2)[1].strip()).tolist()
df['ESTADO'] = estado_lista

# Plotar o número único de IDs por TEMPO para o estado 'CE'
df[df['ESTADO'] == 'CE'].groupby('TEMPO').nunique()['ID'].plot(kind='bar', title='Número de IDs por Tempo para CE')
plt.xlabel('Tempo')
plt.ylabel('Número de IDs')
plt.show()

# Função para contar palavras em um texto
def count_palavras(texto):
    return len(texto.split())

# Plotar o histograma da contagem de palavras na coluna 'DESCRICAO'
df['DESCRICAO'].apply(count_palavras).plot(kind='hist', density=True, title='Distribuição da Contagem de Palavras na Descrição')
plt.xlabel('Número de Palavras')
plt.ylabel('Densidade')
plt.show()

# Plotar a densidade da contagem de palavras na coluna 'DESCRICAO'
df['DESCRICAO'].apply(count_palavras).plot.kde(title='Densidade da Contagem de Palavras na Descrição')
plt.xlabel('Número de Palavras')
plt.ylabel('Densidade')
plt.show()