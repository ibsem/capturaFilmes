import pandas as pd

# para instalar o pandas
# pip install pandas

# url com explicação para upload no firebase
# https://www.py4u.net/discuss/227998

#url da fonte de dados
# https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv

#Caminho do arquivo csv
caminho = '/Users/ibsem/workspaceVisualcode/capturaFilmes/movies_metadata.csv'
df = pd.read_excel()
df = pd.read_csv (caminho)
#visualiza as colunas que deseja e separa num novo dataframe
#print(df.columns)
pd.options.display.max_columns = None
colunas = ['original_title','overview']
df2 = df[colunas]
print (df2.head(10))

# filtra as linhas com a expressão que você escolher 'finance' por exemplo
df3 = df2[df2['overview'].str.contains('finance', na=False)]
#quantidade de linhas
index = df3.index
rows = len(index)
print ('---------------')
print(df3)
print('numero de linhas', rows)
#salva numa planilha

df3.to_excel('/Users/ibsem/workspaceVisualcode/capturaFilmes/filmesPalavrasFinance.xlsx')
varJson = df3.to_json('/Users/ibsem/workspaceVisualcode/capturaFilmes/filmesPalavrasFinance.json')

# depois montar o codigo para carregar no firebase