'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Fundamentos de Programação com Python
Soluções dos Exercícios
'''

## Exercício 2

# Qual será a saída do seguinte snippet de código? 
nome = "Carlos" 
idade = 30 
altura = 1.75 
esta_chovendo = True 

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Está chovendo? {esta_chovendo}") 
 
# Resposta Esperada
# Nome: Carlos, Idade: 30, Altura: 1.75, Está chovendo? True

## Exercício 3
# Escreva um programa em Python que peça ao usuário para inserir seu nome, 
# idade e altura. 
# O programa deve então imprimir essas informações em uma frase completa. 
# Utilize variáveis para armazenar os valores inseridos pelo usuário. 
 
nome = input("Digite seu nome: ") 
idade = int(input("Digite sua idade: ")) 
altura = float(input("Digite sua altura: ")) 
 
print(f"Olá, {nome}! Você tem {idade} anos e sua altura é {altura} metros.") 
