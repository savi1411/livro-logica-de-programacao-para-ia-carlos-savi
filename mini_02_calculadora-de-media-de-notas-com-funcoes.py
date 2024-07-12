'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Miniprojeto: Calculadora de Média de Notas com Funções
'''

# Definição das Funções
def calcular_media(notas): 
    total = sum(notas) 
    quantidade = len(notas) 
    return total / quantidade 
 
def obter_notas(): 
    notas = [] 
    while True: 
        entrada = input("Digite uma nota (ou 'sair' para finalizar): ") 
        if entrada.lower() == 'sair': 
            break 
        try: 
            nota = float(entrada) 
            notas.append(nota) 
        except ValueError: 
            print("Entrada inválida. Por favor, digite um número ou 'sair' para finalizar.") 
    return notas 
 
# Fluxo Principal
print("Bem-vindo à Calculadora de Média de Notas!") 
notas = obter_notas() 
if notas: 
    media = calcular_media(notas) 
    print(f"A média das notas fornecidas é: {media:.2f}") 
else: 
    print("Nenhuma nota foi fornecida.") 
 

 