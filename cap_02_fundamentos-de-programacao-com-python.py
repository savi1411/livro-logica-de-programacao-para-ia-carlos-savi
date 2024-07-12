'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Fundamentos de Programação com Python
'''

## Exemplos de Variáveis 
idade = 25           # Variável inteira 
nome = "Carlos"      # Variável string 
altura = 1.75        # Variável float 
esta_chovendo = True # Variável booleana 
 
# Exibindo os valores das variáveis 
print(idade)         # Saída: 25 
print(nome)          # Saída: Carlos 
print(altura)        # Saída: 1.75 
print(esta_chovendo) # Saída: True 

## Exemplos de Constantes 
PI = 3.14159 
GRAVIDADE = 9.8 
VELOCIDADE_DA_LUZ = 299792458   # em metros por segundo
 
# Exibindo os valores das constantes 
print(PI)               # Saída: 3.14159 
print(GRAVIDADE)        # Saída: 9.8 
print(VELOCIDADE_DA_LUZ)# Saída: 299792458 

## Uso de Constantes em Cálculos 

# Cálculo da área de um círculo 
raio = 5 
area = PI * (raio ** 2) 
print("Área do círculo:", area)  
# Saída: Área do círculo: 78.53975 
 
# Cálculo da força gravitacional 
massa1 = 50  # em kg 
massa2 = 80  # em kg 
distancia = 10  # em metros 
forca = GRAVIDADE * (massa1 * massa2) / (distancia ** 2) 
print("Força gravitacional:", forca)  
# Saída: Força gravitacional: 392.0 

## Exemplo de Entrada de Dados: 

# Solicitando a entrada do usuário e armazenando em uma variável 
nome = input("Digite seu nome: ") 

# Convertendo a entrada para inteiro 
idade = int(input("Digite sua idade: "))   
 
# Exibindo os valores fornecidos pelo usuário 
print("Nome:", nome) 
print("Idade:", idade) 
 
 ## Exemplo de Saída de Dados 

# Exibindo uma mensagem simples 
print("Hello, World!") 
 
# Exibindo múltiplos valores 
nome = "Alice" 
idade = 30 
print("Nome:", nome, "Idade:", idade)

## Exemplo Combinado de Entrada e Saída de Dados 

# Solicitando a entrada do usuário 
numero1 = float(input("Digite o primeiro número: ")) 
numero2 = float(input("Digite o segundo número: ")) 
 
# Calculando a soma, diferença, produto e quociente 
soma = numero1 + numero2 
diferenca = numero1 - numero2 
produto = numero1 * numero2 
quociente = numero1 / numero2 if numero2 != 0 else "Indefinido (divisão por zero)" 
 
# Exibindo os resultados 
print("A soma dos números é:", soma) 
print("A diferença dos números é:", diferenca) 
print("O produto dos números é:", produto) 
print("O quociente dos números é:", quociente) 

## Exemplo com f-string: 
nome = "Carlos" 
idade = 30 
print(f"Meu nome é {nome} e eu tenho {idade} anos.") 

## Exemplo de formatação de números com f-string: 
media = 7.12345
print(f"Média das notas: {media:.2f}") 

## Outras Formas de Formatação 

# Método .format(): 
nome = "Carlos" 
idade = 30 
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade)) 

# Operador % (mais antigo, mas mesmo resultado): 
nome = "Carlos" 
idade = 30 
print("Meu nome é %s e eu tenho %d anos." % (nome, idade)) 

## Tipos de Dados em Python 

# Inteiros (int): 
quantidade = 4 
numero_negativo = -10 
print(quantidade, numero_negativo) 
# Saída: 4 -10 

# Flutuantes (float)
preco = 19.99 
pi = 3.14159 
print(preco, pi) 
# Saída: 19.99 3.14159   

# Strings (str)
nome = "Alice" 
mensagem = "Olá, " + nome + "!" 
print(mensagem) 
# Saída: Olá, Alice! 

# Booleanos (bool)
esta_chovendo = True 
feriado = False 
print(esta_chovendo, feriado) 
# Saída: True False  
