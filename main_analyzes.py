# Importando as bibliotecas
import pandas as pd

# Importando a base de dados
tabela_geral =pd.read_csv('Minicurso Análise de Dados no Python/ClientesBanco.csv', encoding = 'latin1')
pd.set_option('display.max_columns', None)
print(tabela_geral)
