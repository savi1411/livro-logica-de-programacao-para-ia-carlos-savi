'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Estrutura de Dados
Soluções dos Exercícios
'''

## Exercício 2

# O seguinte código contém um erro de sintaxe. 
# Identifique e corrija o erro. 

'''
frutas = ["maçã", "banana", "cereja" 
frutas.append("laranja") 
print(frutas) 
'''

# Resposta: O erro está na falta de um colchete de fechamento "]" 
# na definição da lista frutas. 

# Código corrigido 
frutas = ["maçã", "banana", "cereja"] 
frutas.append("laranja") 
print(frutas) 
 
## Exercício 3

# Escreva um programa em Python que crie um dicionário 
# para armazenar informações sobre vários alunos. 
# O programa deve permitir adicionar novos alunos 
# com suas respectivas notas em três disciplinas 
# (Matemática, Português e Ciências). 
# Em seguida, o programa deve calcular 
# e exibir a média das notas de cada aluno. 

# Exemplo de Solução:

# Função para adicionar alunos ao dicionário 
def adicionar_aluno(dicionario_alunos, nome, notas): 
    dicionario_alunos[nome] = notas 
 
# Função para calcular a média das notas de um aluno 
def calcular_media(notas): 
    return sum(notas) / len(notas) 
 
# Dicionário para armazenar os dados dos alunos 
alunos = {} 
 
# Adicionando alunos ao dicionário 
adicionar_aluno(alunos, "Carlos", [8, 7, 9]) 
adicionar_aluno(alunos, "Ana", [10, 9, 10]) 
adicionar_aluno(alunos, "João", [6, 5, 8]) 
 
# Calculando e exibindo a média das notas de cada aluno 
for aluno, notas in alunos.items(): 
    media = calcular_media(notas) 
    print(f"Média das notas de {aluno}: {media:.2f}") 
