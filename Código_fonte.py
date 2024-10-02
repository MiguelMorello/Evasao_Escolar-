import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ler o arquivo CSV
df = pd.read_csv('/content/sample_data/a.csv')

# Selecionar as colunas de interesse
df_selected = df[['Ano', 'Unidade_Geografica', 'Taxa_Abandono', 'Renda_Media']]

# Agrupar os dados por ano e região e calcular a média da taxa de abandono e renda mensal
df_grouped = df_selected.groupby(['Ano', 'Unidade_Geografica']).agg({'Taxa_Abandono': 'mean', 'Renda_Media': 'mean'})


# Gráfico de pizza (Exemplo para o ano de 2023)
df_2023 = df_grouped.loc[2023]
plt.figure(figsize=(8, 8))
plt.pie(df_2023['Taxa_Abandono'], labels=df_2023.index, autopct='%1.1f%%', startangle=90)
plt.title('Taxa de Abandono por Região em 2023')
plt.show()

# Adicionar um espaço
plt.figure(figsize=(1, 1))
plt.axis('off')
plt.show()

# Boxplot (Exemplo para a Taxa de Abandono ao longo dos anos)
plt.figure(figsize=(12, 8))
plt.boxplot([df_grouped.loc[ano]['Taxa_Abandono'] for ano in df_grouped.index.get_level_values('Ano').unique()],
            labels=df_grouped.index.get_level_values('Ano').unique())
plt.xlabel('Ano')
plt.ylabel('Taxa de Abandono')
plt.title('Distribuição da Taxa de Abandono ao longo dos Anos')
plt.show()

# Adicionar um espaço
plt.figure(figsize=(1, 1))
plt.axis('off')
plt.show()

# Gráfico de dispersão (Exemplo para a relação entre a taxa de abandono e a renda média)
# Crie um modelo de regressão linear
z = np.polyfit(df_grouped['Renda_Media'], df_grouped['Taxa_Abandono'], 1)
p = np.poly1d(z)

# Gráfico de linha para a relação entre a renda média e a taxa de abandono
plt.figure(figsize=(12, 8))
plt.plot(df_grouped['Renda_Media'], df_grouped['Taxa_Abandono'], 'o', label='Dados')
plt.plot(df_grouped['Renda_Media'], p(df_grouped['Renda_Media']), "r--", label='Regressão Linear')
plt.xlabel('Renda Média')
plt.ylabel('Taxa de Abandono')
plt.title('Relação entre Renda Média e Taxa de Abandono')
plt.legend()
plt.show()


# Adicionar um espaço
plt.figure(figsize=(1, 1))
plt.axis('off')
plt.show()

# Grafico entre região e salario
# Agrupa os dados por região e calcula o salário médio
df_grouped = df.groupby('Unidade_Geografica')['Renda_Media'].mean().reset_index()

# Gráfico de barras para a relação entre as regiões e o salário médio
plt.figure(figsize=(12, 8))
plt.bar(df_grouped['Unidade_Geografica'], df_grouped['Renda_Media'])
plt.xlabel('Região')
plt.ylabel('Salário Médio')
plt.title('Relação entre Regiões e Salário Médio')
plt.xticks(rotation=90)  # Rotaciona os nomes das regiões para melhor visualização
plt.show()
