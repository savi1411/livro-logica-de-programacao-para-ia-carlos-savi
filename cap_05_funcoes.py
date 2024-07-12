'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Funções
'''

## Exemplos de Funções Internas: 

# len(): Retorna o comprimento de uma lista, string, ou outra coleção. 
tamanho = len("Python") 
print(tamanho)  # Saída: 6 

#max(): Retorna o valor máximo de uma sequência. 
maior = max([10, 20, 30]) 
print(maior)  # Saída: 30 

# min(): Retorna o valor mínimo de uma sequência. 
menor = min([10, 20, 30]) 
print(menor)  # Saída: 10 

## Exemplos de Funções de Conversão de Tipos: 

# int(): Converte um valor para inteiro. 
numero = int("10") 
print(numero)  # Saída: 10 
 
# float(): Converte um valor para ponto flutuante. 
numero = float("10.5") 
print(numero)  # Saída: 10.5 
 
# str(): Converte um valor para string. 
texto = str(10) 
print(texto)  # Saída: "10" 

## Exemplos de Funções Matemáticas: 

# math.sqrt(): Calcula a raiz quadrada de um número. 
import math 
raiz = math.sqrt(16) 
print(raiz)  # Saída: 4.0 
 
# math.pow(): Calcula a potência de um número. 
potencia = math.pow(2, 3) 
print(potencia)  # Saída: 8.0 
 
# math.sin(), math.cos(), math.tan(): Calcula o seno, cosseno e tangente de um ângulo. 
angulo = math.radians(45) 
seno = math.sin(angulo) 
print(seno)  # Saída: 0.7071067811865475 

## Exemplo de Função Personalizada: 

# Define a função saudacao()
def saudacao(): 
    print("Olá, Mundo!") 

# Chama a função  
saudacao()

## Exemplo de Função com Argumento: 
def saudacao(nome): 
    print(f"Olá, {nome}!") 

# Passa "Carlos" como argumento para a função saudacao 
saudacao("Carlos")

## Exemplo Função com Retorno: 
def soma(a, b): 
    return a + b 
 
resultado = soma(3, 5) 
print(resultado)  # Saída: 8

## Exemplo de Função com vários Argumentos: 
def multiplicar(a, b, c): 
    return a * b * c 
 
resultado = multiplicar(2, 3, 4) 
print(resultado)  # Saída: 24 

## Exemplo de Função com Argumento Padrão: 

def saudacao(nome="Mundo"): 
    print(f"Olá, {nome}!") 
 
# Usa o valor padrão "Mundo" 
saudacao() 

# Usa o valor "Carlos"		 
saudacao("Carlos")

## Exemplo de Função Recursiva: 
def fatorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * fatorial(n - 1) 
 
print(fatorial(5))  # Saída: 120 

## Exemplo de Uso em IA: Função para Normalização de Dados 
def normalizar(dados): 
    minimo = min(dados) 
    maximo = max(dados) 
    normalizados = [(x - minimo) / (maximo - minimo) for x in dados] 
    return normalizados 
 
dados = [10, 20, 30, 40, 50] 
dados_normalizados = normalizar(dados) 
print(dados_normalizados)  # Saída: [0.0, 0.25, 0.5, 0.75, 1.0] 

 
 

 
 

 