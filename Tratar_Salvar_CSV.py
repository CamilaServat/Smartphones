import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine

class DatasetManipulation:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, sep=';')  
        print("Dados carregados com sucesso.")

        # Renomeando as colunas do DataFrame para tornar mais fácil o entendimento
        self.df.columns = [
            'marca', 'modelo', 'preco', 'avaliacao_media', '5G_disponivel', 'marca_processador',
            'num_nucleos', 'velocidade_processador', 'capacidade_bateria', 'carregamento_rapido_disponivel',
            'carregamento_rapido', 'capacidade_ram', 'memoria_interna', 'tamanho_tela', 'taxa_refrescamento',
            'num_cameras_traseiras', 'sistema_operacional', 'camera_principal_traseira', 'camera_principal_frontal',
            'memoria_expansivel_disponivel', 'altura_resolucao', 'largura_resolucao'
        ]

        print("Primeiras linhas do dataset:")
        print(self.df.head())  

        print("\nInformacoes sobre o dataset:")
        print(self.df.info())  

        print("\nEstatisticas descritivas (apenas colunas numericas):")
        print(self.df.describe())  

        print("\nValores nulos por coluna:")
        print(self.df.isnull().sum())  

    def limpar_dados(self):
        # Preenche os valores nulos nas colunas com a mediana ou moda
        self.df['avaliacao_media'] = self.df['avaliacao_media'].fillna(self.df['avaliacao_media'].median())
        self.df['marca_processador'] = self.df['marca_processador'].fillna(self.df['marca_processador'].mode()[0])
        self.df['num_nucleos'] = self.df['num_nucleos'].fillna(self.df['num_nucleos'].median())
        self.df['velocidade_processador'] = self.df['velocidade_processador'].fillna(self.df['velocidade_processador'].median())
        self.df['capacidade_bateria'] = self.df['capacidade_bateria'].fillna(self.df['capacidade_bateria'].median())
        self.df['carregamento_rapido'] = self.df['carregamento_rapido'].fillna(self.df['carregamento_rapido'].median())
        self.df['sistema_operacional'] = self.df['sistema_operacional'].fillna(self.df['sistema_operacional'].mode()[0])
        self.df['camera_principal_traseira'] = self.df['camera_principal_traseira'].fillna(self.df['camera_principal_traseira'].median())
        self.df['camera_principal_frontal'] = self.df['camera_principal_frontal'].fillna(self.df['camera_principal_frontal'].median())

        print("Dados limpos com sucesso.")

    def transformar_dados(self):
        self.df['preco'] = self.df['preco'] * 0.06  
        self.df['preco'] = self.df['preco'].round(2)  
        print("Precos convertidos para reais e arredondados para 2 casas decimais.")

    def salvar_dados(self, path):
        self.df.to_csv(path, index=False, sep=';')  
        print(f"Dados salvos em {path}")

    def salvar_dados_mysql(self, host, user, password, database, table_name):
        try:
            # Cria a conexão com o banco de dados MySQL usando SQLAlchemy
            engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
            self.df.to_sql(table_name, con=engine, if_exists='replace', index=False)  
            print(f"Dados salvos com sucesso na tabela '{table_name}' do banco de dados '{database}'.")
        except Exception as e:
            print(f"Erro ao salvar dados no MySQL: {e}")  

# Caminho do arquivo CSV de entrada
csv_path = r'c:\Users\Camila\Documents\Ciência dos Dados\Smartphones.csv'

dataset = DatasetManipulation(csv_path)

dataset.limpar_dados()

dataset.transformar_dados()

# Caminho de saída para o arquivo CSV transformado
output_path = r'c:\Users\Camila\Documents\Ciência dos Dados\Smartphones_Transformado.csv'
dataset.salvar_dados(output_path)

# Configuração do banco de dados MySQL
host = 'localhost'  
user = 'root'       
password = ''  
database = 'smartphones'  
table_name = 'dados_smartphones'

dataset.salvar_dados_mysql(host, user, password, database, table_name)