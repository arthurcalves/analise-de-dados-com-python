# Caminho do arquivo CSV.
caminho_dados = "C:\\Users\\Nicolas\\Documents\\Projetos Python\\Análise de dados com Python e Pandas\\2025_20260920_Viagens\\2025_Viagem.csv"

import pandas as pd # type: ignore

# Lê o CSV usando ';' como separador e a codificação do arquivo.
pd.set_option('display.max_columns', None)  # Exibir todas as colunas
df_viagem = pd.read_csv(caminho_dados, encoding='Windows-1252', sep=';')

print(df_viagem)

# Seleciona e exibe colunas específicas.
df_viagem["Valor passagens"]
print(df_viagem["Valor passagens"])
df_viagem['CPF viajante']
print(df_viagem['CPF viajante'])

colunas_desejadas = ['CPF viajante', 'Valor passagens']
df_viagem[colunas_desejadas]
print(df_viagem[colunas_desejadas])

# Exemplos de operações de texto: maiúsculas, tamanho e substituição.
df_viagem['Nome do órgão superior'].str.upper()
print(df_viagem['Nome do órgão superior'].str.upper())
df_viagem['Nome do órgão superior'].str.len()
print(df_viagem['Nome do órgão superior'].str.len())
df_viagem['Nome do órgão superior'].str.upper().str.replace('MINISTÉRIO', 'MIN.')
print(df_viagem['Nome do órgão superior'].str.upper().str.replace('MINISTÉRIO', 'MIN.'))

# Antes da conversão, os valores podem ser texto; nesse caso, '+' pode concatená-los.
df_viagem[['Valor diárias', 'Valor passagens']]
print(df_viagem[['Valor diárias', 'Valor passagens']])
df_viagem['Valor diárias'] + df_viagem['Valor passagens']
print(df_viagem['Valor diárias'] + df_viagem['Valor passagens'])

# Troca a vírgula decimal por ponto e converte as colunas de valores para números.
df_viagem['Valor diárias'] = df_viagem['Valor diárias'].str.replace(',', '.').astype(float)
df_viagem['Valor passagens'] = df_viagem['Valor passagens'].str.replace(',', '.').astype(float)
df_viagem['Valor devolução'] = df_viagem['Valor devolução'].str.replace(',', '.').astype(float)
df_viagem['Valor outros gastos'] = df_viagem['Valor outros gastos'].str.replace(',', '.').astype(float)

# Confere os tipos de dados e soma diárias e passagens para cada viagem.
df_viagem.info()
df_viagem['Valor diárias'] + df_viagem['Valor passagens']
print(df_viagem['Valor diárias'] + df_viagem['Valor passagens'])

# Cria e exibe o total dessas despesas para cada viagem.
df_viagem['Despesas'] = df_viagem['Valor diárias'] + df_viagem['Valor passagens'] + df_viagem['Valor outros gastos']
print(df_viagem['Despesas'])

# Calcula a porcentagem de viagens por cargo.
(df_viagem['Cargo'].value_counts(normalize=True) * 100).rename('Proporção de viagens').reset_index()
print((df_viagem['Cargo'].value_counts(normalize=True) * 100).rename('Proporção de viagens').reset_index())
