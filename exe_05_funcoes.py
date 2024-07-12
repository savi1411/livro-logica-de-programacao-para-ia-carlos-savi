'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Funções
Soluções dos Exercícios
'''

## Exercício 2

# O snippet de código contém um erro de sintaxe. 
# Identifique e corrija o erro para que o código funcione corretamente. 

'''
def saudacao(nome): 
    print(f"Olá, {nome}!") 
     
saudacoes("Carlos") 
'''

# Resposta: O nome da função estava inconsistente. 
# Aqui está o código corrigido: 
def saudacao(nome): 
    print(f"Olá, {nome}!") 
     
saudacao("Carlos") 
 
## Exercício 3

# Escreva uma função personalizada chamada maior que receba 
# três números inteiros e retorne qual o maior desses números. 
# Em seguida, solicite ao usuário a digitação de três números, 
# passe os números digitados como argumentos da função e imprima o retorno da função. 

# Solução: 
def maior(a, b, c): 
    maior_numero = a  # Suponha que a seja o maior 
    if b > maior_numero: 
        maior_numero = b 
    if c > maior_numero: 
        maior_numero = c 
    return maior_numero 
 
# Solicitando ao usuário para inserir três números inteiros 
num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: ")) 
num3 = int(input("Digite o terceiro número: ")) 
 
# Calculando o maior número usando a função maior 
resultado = maior(num1, num2, num3) 
print(f"O maior dos três números fornecidos é: {resultado}") 
