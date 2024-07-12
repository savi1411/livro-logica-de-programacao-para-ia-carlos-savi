'''                                                                                             $
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Miniprojeto: Sistema de Recomedação de Filmes com IA
'''

import pandas as pd 
 
# Passo 1: Criando o DataFrame com filmes e características 
filmes = { 
    'Título': ['Filme A', 'Filme B', 'Filme C', 'Filme D'], 
    'Gênero': ['Ação', 'Comédia', 'Ação', 'Drama'], 
    'Duração': [120, 90, 150, 110], 
    'Ano': [2010, 2015, 2012, 2018], 
    'Avaliação': [4.5, 3.5, 4.0, 5.0] 
} 
df_filmes = pd.DataFrame(filmes)                                                                        
print(df_filmes) 

from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics.pairwise import cosine_similarity 
 
# Passo 2: Convertendo os gêneros para valores numéricos 
le = LabelEncoder() 
df_filmes['Gênero'] = le.fit_transform(df_filmes['Gênero']) 
 
# Calculando a similaridade coseno 
similaridade = cosine_similarity(df_filmes[['Gênero', 'Duração', 'Ano', 'Avaliação']]) 
print(similaridade) 
 

# Passo 3: Função de Recomendação 
def recomendar_filmes(titulo, similaridade, df_filmes): 
    # Encontrando o índice do filme 
    indice_filme = df_filmes[df_filmes['Título'] == titulo].index[0] 
     
    # Calculando a similaridade dos filmes 
    similaridades = list(enumerate(similaridade[indice_filme])) 
     
    # Ordenando os filmes pela similaridade 
    similaridades = sorted(similaridades, key=lambda x: x[1], reverse=True) 
     
    # Pegando os 3 filmes mais similares 
    recomendacoes = [df_filmes['Título'][i[0]] for i in similaridades[1:4]] 
    return recomendacoes 
 
# Exemplo de recomendação 
titulo_filme = 'Filme A' 
recomendacoes = recomendar_filmes(titulo_filme, similaridade, df_filmes) 
print(f"Filmes recomendados para quem gostou de {titulo_filme}: {recomendacoes}") 

