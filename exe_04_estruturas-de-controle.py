'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Estruturas de Controle
Soluções dos Exercícios
'''

## Exercício 1

# Explique a diferença entre as estruturas de controle if, elif e else 
# em Python e forneça um exemplo de quando cada uma seria usada. 

# Resposta: As estruturas de controle if, elif e else são usadas 
# para tomar decisões no código com base em condições específicas: 

# Exemplo de Solução:
nota = 85 
 
if nota >= 90: 
    print("Excelente") 
elif nota >= 75: 
    print("Bom") 
elif nota >= 60: 
    print("Satisfatório") 
else: 
    print("Insuficiente") 
 
## Exercício 2

# Explique a diferença entre os loops for e while em Python 
# e forneça um exemplo de quando cada um seria usado. 

'''
Resposta: Os loops for e while são usados para repetir um bloco de código 
    várias vezes, mas de maneiras diferentes:

for é usado para iterar sobre uma sequência (como uma lista, tupla ou string) 
    ou um intervalo de números. 
    Ele é mais adequado quando você sabe o número de iterações 
    ou está percorrendo uma coleção de elementos. 
while é usado para repetir um bloco de código enquanto uma condição 
    específica for verdadeira. 
    É útil quando o número de iterações não é conhecido previamente 
    e depende de uma condição. 
'''

# Exemplo de solução de Loop for: 

# Percorrendo uma lista de frutas 
frutas = ["maçã", "banana", "cereja"] 
for fruta in frutas: 
    print(fruta) 
 
# Exemplo de solução de Loop while: 

# Imprimindo números de 1 a 5 
contador = 1 
while contador <= 5: 
    print(contador) 
    contador += 1 

## Exercício 3

# O código a seguir tem problemas de indentação. 
# Corrija-o para que funcione corretamente sem erros de sintaxe. 

'''
numero = 10 
if numero > 0: 
print("Número positivo") 
if numero % 2 == 0: 
print("Número par") 
else: 
print("Número ímpar") 
else: 
print("Número negativo") 
'''

# Solução: 
numero = 10 
if numero > 0: 
    print("Número positivo") 
    if numero % 2 == 0: 
        print("Número par") 
    else: 
        print("Número ímpar") 
else: 
    print("Número negativo") 

## Exerçicio 4

# Escreva um programa em Python que percorra uma lista de números 
# de 1 a 10 e imprima "Número par" se o número for par, 
# e "Número ímpar" se o número for ímpar. 
# Use um loop for e uma estrutura condicional if-else. 

# Exemplo de Solução: 

# Lista de números de 1 a 10 
numeros = list(range(1, 11)) 

# Percorrendo a lista com um loop for 
for numero in numeros: 
    if numero % 2 == 0: 
        print(numero, "é Número par") 
    else: 
        print(numero, "é Número ímpar") 
