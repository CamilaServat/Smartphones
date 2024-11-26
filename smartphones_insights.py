import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine(f"mysql+pymysql://root:@localhost/smartphones")

# Carregar dados do banco de dados
df = pd.read_sql('SELECT * FROM dados_smartphones', con=engine)

# Gráfico 1: Preço médio por marca - Gráfico de Barras
marca_preco = df.groupby('marca')['preco'].mean().sort_values(ascending=False)
plt.figure(figsize=(20, 8))  # Ajustando o tamanho da figura
sns.barplot(x=marca_preco.index, y=marca_preco.values, palette='viridis', hue=marca_preco.index)
plt.title('Preço médio por marca')
plt.xlabel('Marca')
plt.ylabel('Preço Médio (R$)')
plt.xticks(rotation=90)  # Rotação dos rótulos para melhorar a legibilidade
plt.tight_layout()
plt.show()

# Gráfico 2: Avaliação média por marca - Gráfico de Barras
marca_avaliacao = df.groupby('marca')['avaliacao_media'].mean().sort_values(ascending=False)
plt.figure(figsize=(20, 8))
sns.barplot(x=marca_avaliacao.index, y=marca_avaliacao.values, palette='Blues', hue=marca_avaliacao.index)
plt.title('Avaliação média por marca')
plt.xlabel('Marca')
plt.ylabel('Avaliação Média')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico 3: Número médio de núcleos do processador por marca - Gráfico de Barras
marca_nucleos = df.groupby('marca')['num_nucleos'].mean().sort_values(ascending=False)
plt.figure(figsize=(20, 8))
sns.barplot(x=marca_nucleos.index, y=marca_nucleos.values, palette='coolwarm', hue=marca_nucleos.index)
plt.title('Número médio de núcleos do processador por marca')
plt.xlabel('Marca')
plt.ylabel('Número Médio de Núcleos')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico 4: Capacidade de bateria média por marca - Gráfico de Barras
marca_bateria = df.groupby('marca')['capacidade_bateria'].mean().sort_values(ascending=False)
plt.figure(figsize=(20, 8))
sns.barplot(x=marca_bateria.index, y=marca_bateria.values, palette='muted', hue=marca_bateria.index)
plt.title('Capacidade de bateria média por marca')
plt.xlabel('Marca')
plt.ylabel('Capacidade de Bateria (mAh)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Gráfico 5: Distribuição de smartphones por sistema operacional - Gráfico de Pizza
sistema_operacional_counts = df['sistema_operacional'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(sistema_operacional_counts, labels=sistema_operacional_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2', len(sistema_operacional_counts)))
plt.title('Distribuição de smartphones por sistema operacional')
plt.show()

# Gráfico 6: Distribuição de smartphones com 5G - Gráfico de Pizza
df_5g = df['5G_disponivel'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(df_5g, labels=df_5g.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set1', len(df_5g)))
plt.title('Distribuição de smartphones com 5G')
plt.show()

# Gráfico 7: Distribuição do tipo de carregamento rápido - Gráfico de Pizza
carregamento_rapido_counts = df['carregamento_rapido_disponivel'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(carregamento_rapido_counts, labels=carregamento_rapido_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('coolwarm', len(carregamento_rapido_counts)))
plt.title('Distribuição de smartphones com carregamento rápido disponível')
plt.show()
