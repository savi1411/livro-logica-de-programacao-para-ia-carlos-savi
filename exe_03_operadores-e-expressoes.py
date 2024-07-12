'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Operadores e Expressões
Soluções dos Exercícios
'''

## Exercício 2

# Qual será a saída do seguinte snippet de código? 
# (Verdadeiro (True) ou Falso (False)) 

a = 10 
b = 5 
resultado = (a > b) and (a != b) 
print(resultado) 
 
# Resposta esperada: True

## Exercício 3

# Escreva um programa em Python que peça ao usuário para inserir 
# dois números e depois imprima a soma, a diferença, o produto 
# e o quociente desses números. 
# Use variáveis para armazenar os números e comandos de saída para exibir os resultados. Utilize operadores aritméticos e formatação de strings. 

num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: ")) 
 
soma = num1 + num2 
diferenca = num1 - num2 
produto = num1 * num2 
quociente = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)" 
 
print(f"A soma dos números é: {soma}") 
print(f"A diferença dos números é: {diferenca}") 
print(f"O produto dos números é: {produto}") 
print(f"O quociente dos números é: {quociente}")

