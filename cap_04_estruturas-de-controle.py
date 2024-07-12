'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Estruturas de Controle
'''

## Exemplo de Indentação Correta com if-else 

# Usando if else com duas instruções em cada bloco 
idade = 20 
 
if idade >= 18: 
    print("Você é maior de idade.") 
    print("Pode votar nas eleições.") 
else: 
    print("Você é menor de idade.") 
    print("Não pode votar nas eleições.") 


## Exemplo de Indentação Incorreta 

# Exemplo com indentação incorreta 
idade = 20 

# Remova os comentários para visualizar o erro

# if idade >= 18:
# print("Você é maior de idade.") 
# print("Pode votar nas eleições.") 
# else: 
# print("Você é menor de idade.") 
# print("Não pode votar nas eleições.") 

## Exemplo de Estrutura Condicional 
idade = 18 
 
if idade < 18: 
    print("Menor de idade") 
elif idade == 18: 
    print("Recém-maior de idade") 
else: 
    print("Maior de idade") 
 
# Uso de Condições para Verificação 
numero = 10 
 
if numero % 2 == 0: 
    print("Número par") 
else: 
    print("Número ímpar") 

## Exemplo de Estrutura Condicional com elif: 
nota = 85 
 
if nota >= 90: 
    print("Excelente") 
elif nota >= 75: 
    print("Bom") 
elif nota >= 60: 
    print("Satisfatório") 
else: 
    print("Insuficiente") 

## Exemplo Prático de Entrada de Dados com try except: 

entrada = input("Digite um número: ") 
 
try: 
    numero = float(entrada) 
    if numero > 0: 
        print("O número é positivo.") 
    elif numero < 0: 
        print("O número é negativo.") 
    else: 
        print("O número é zero.") 
except ValueError: 
    print("Entrada inválida. Por favor, digite um número válido.") 

## Exemplo de Loop for 
frutas = ["maçã", "banana", "cereja"] 
 
for fruta in frutas: 
    print(fruta) 

## Exemplo prático de Loop for 
notas = [7.5, 8.0, 6.5, 9.0, 8.5] 
soma = 0 
 
for nota in notas: 
    soma += nota 
 
media = soma / len(notas) 
print(f"A média das notas é {media:.2f}") 

## Exemplo de Loop while com Contador 
contador = 0 
 
while contador < 5: 
    print(f"Contador é {contador}") 
    contador += 1 

## Exemplo prático com Loop while 
soma = 0 
numero = 1 
 
while numero <= 10: 
    soma += numero 
    numero += 1 
 
print(f"A soma dos números de 1 a 10 é {soma}") 

## Exemplo de Combinação de Loops e Condições 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 
for numero in numeros: 
    if numero % 2 == 0: 
        print(numero, "é par") 
    else: 
        print(numero, "é ímpar") 
 
## Exemplo de Loop Infinito 
# Para testar, remova os comentários
# contador = 0 
# while contador < 5: 
#     print("Contador é:", contador) 
    # Falta incrementar o contador, resultando em um loop infinito 
    # Para interromper o loop digite <control+c>

## Como Evitar o Loop Infinito 
contador = 0 
while contador < 5: 
    print("Contador é:", contador) 
    contador += 1  # Atualizando a condição de término 

## Exemplo de continue: 
for numero in range(1, 11): 
    if numero % 2 == 0: 
        continue  # Pula a iteração se o número for par 
    print(numero) 

## Exemplo de break: 
for numero in range(1, 11): 
    if numero == 5: 
        break  # Sai do loop quando o número é 5 
    print(numero) 
 
## Exemplo de Uso em IA: Implementação de uma Árvore de Decisão Simples

# Coletando os atributos da fruta 
peso = float(input("Digite o peso da fruta (em gramas): ")) 
cor = input("Digite a cor da fruta (vermelho, amarelo, verde): ").lower() 
 
# Classificação baseada em peso e cor 
if peso > 150 and cor == "vermelho": 
    classificacao = "Maçã" 
elif peso <= 150 and cor == "amarelo": 
    classificacao = "Banana" 
elif peso < 50 and cor == "vermelho": 
    classificacao = "Cereja" 
else: 
    classificacao = "Fruta desconhecida" 
 
# Exibindo a classificação 
print(f"A fruta é classificada como: {classificacao}") 

