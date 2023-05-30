# Importando as bibliotecas
import pandas as pd

# Importando a base de dados
# Necessário inserir o encoding pelos caracteres que contém no ClientesBanco.csv
tabela_geral = pd.read_csv('Minicurso Análise de Dados no Python/ClientesBanco.csv', encoding='latin1')

# Tratamento da base de dados
print(f'{tabela_geral}\n')
pd.set_option('display.max_columns', None)
tabela_geral = tabela_geral.drop('CLIENTNM', axis=1)







