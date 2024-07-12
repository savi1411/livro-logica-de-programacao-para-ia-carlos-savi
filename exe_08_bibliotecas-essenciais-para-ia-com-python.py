'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Bibliotecas Essenciais para IA com Python
Soluções dos Exercícios
'''

## Exercício 2

# Considere o código abaixo que utiliza a biblioteca NumPy. 
# Identifique e corrija os erros de sintaxe no código. 

'''
import numpy as np 
 
array = np.array(1, 2, 3, 4, 5) 
media = lista.mean() 
soma = lista.sum() 
 
print(f"A média do array é {media} e a soma do array é {soma") 
'''
 

# Resposta: O código possui os seguintes erros: 
#   O array foi criado com o nome array mas, na sequência do código, 
#       foi utilizado indevidamente o nome lista para cálculo da media e da soma. 
#   Na função de formatação da string do comando print está faltando 
#       a chave de fechamento. 

# Código corrigido:
import numpy as np  

array = np.array([1, 2, 3, 4, 5])  
media = array.mean()  
soma = array.sum()  

print(f"A média do array é {media} e a soma do array é {soma}") 

# Saída esperada: 
# A média do array é 3.0 e a soma do array é 15 

## Exercício 3

# Utilize a biblioteca Matplotlib para criar um gráfico de barras 
# que exiba as vendas de produtos em uma loja. 
# Os dados são fornecidos abaixo: 

'''
Produtos = 'Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E' 
Vendas = 50, 80, 90, 70, 100
''' 

# DICA: Temos um exemplo semelhante na parte teórica do capítulo, 
# porém naquele exemplo o gráfico gerado foi o de linhas e não de barras. 

# Exemplo de Solução:
import matplotlib.pyplot as plt 
 
# Dados de vendas 
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'] 
vendas = [50, 80, 90, 70, 100] 
 
# Criando o gráfico de barras 
plt.bar(produtos, vendas) 
plt.xlabel('Produtos') 
plt.ylabel('Vendas') 
plt.title('Vendas de Produtos na Loja') 
plt.show()
