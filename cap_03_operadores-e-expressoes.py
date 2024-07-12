'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Operadores e Expressões
'''

## Operadores

## Exemplos de Uso dos Operadores Aritméticos 

# Adição
a = 10 
b = 5 
soma = a + b 
print("Soma:", soma)   
# Saída: Soma: 15 
 
# Subtração 
subtracao = a - b 
print("Subtração:", subtracao)   
# Saída: Subtração: 5 
 
# Multiplicação 
multiplicacao = a * b 
print("Multiplicação:", multiplicacao)   
# Saída: Multiplicação: 50 
 
# Divisão 
divisao = a / b 
print("Divisão:", divisao)   
# Saída: Divisão: 2.0 
 
# Módulo 
modulo = a % b 
print("Módulo:", modulo)   
# Saída: Módulo: 0 
 
# Exponenciação 
exponenciacao = a ** b 
print("Exponenciação:", exponenciacao)   
# Saída: Exponenciação: 100000 
 
# Divisão inteira 
divisao_inteira = a // b 
print("Divisão inteira:", divisao_inteira)   
# Saída: Divisão inteira: 2 

## Exemplos de Uso de Operadores de Atribuição Composta 

# Operador: += 
x = 5 
x += 3  # Equivalente a x = x + 3 
print(x)  # Saída: 8 

# Operador: -= 
y = 10 
y -= 4  # Equivalente a y = y - 4 
print(y)  # Saída: 6 
 
# Operador: *= 
z = 7 
z *= 2  # Equivalente a z = z * 2 
print(z)  # Saída: 14 

# Operador: /= 
w = 20 
w /= 5  # Equivalente a w = w / 5 
print(w)  # Saída: 4.0 
 
## Exemplos de Uso dos Operadores de Comparação 

# Igualdade 
a = 10 
b = 5 
igualdade = (a == b) 
print("Igualdade:", igualdade)   
# Saída: Igualdade: False 
 
# Desigualdade (diferente) 
desigualdade = (a != b) 
print("Desigualdade:", desigualdade)   
# Saída: Desigualdade: True 
 
# Maior que 
maior_que = (a > b) 
print("Maior que:", maior_que)   
# Saída: Maior que: True 
 
# Menor que 
menor_que = (a < b) 
print("Menor que:", menor_que)   
# Saída: Menor que: False 
 
# Maior ou igual a 
maior_ou_igual = (a >= b) 
print("Maior ou igual a:", maior_ou_igual)   
# Saída: Maior ou igual a: True 
 
# Menor ou igual a 
menor_ou_igual = (a <= b) 
print("Menor ou igual a:", menor_ou_igual)   
# Saída: Menor ou igual a: False 

## Exemplos de Uso dos Operadores Lógicos 

# Operador and 
a = True 
b = False 
resultado_and = a and b 
print("Resultado AND:", resultado_and)   
# Saída: Resultado AND: False 
 
# Operador or 
resultado_or = a or b 
print("Resultado OR:", resultado_or)   
# Saída: Resultado OR: True 
 
# Operador not 
resultado_not = not a 
print("Resultado NOT:", resultado_not)   
# Saída: Resultado NOT: False 

# Operador xor 
resultado_xor = a ^ b  
print("Resultado XOR:", resultado_xor)  
# Saída: Resultado XOR: True 

## Exemplo de Expressões e Ordem das Operações 
resultado = 5 + 2 * 3   
# Primeiro multiplicação, depois adição 
print(resultado) 
# Saída: 11 

# Colocando os parêntesis para realçar a precedência
resultado = (5 + 2) * 3   
# Primeiro a expressão entre parênteses 
print(resultado)   
# Saída: 21 

## Exemplo de Comentários 

# Este é um comentário de linha única 
print("Olá, Mundo!")	# Comentário após declaração 
 
''' 
Este é um comentário de múltiplas linhas. 
Pode ser usado para explicar blocos maiores de código. 
''' 
print("Isso também é parte do código.")

 
 