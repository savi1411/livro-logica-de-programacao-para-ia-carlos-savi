'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Miniprojeto: Calculadora de Média de Notas
'''

# Inicializando a lista de notas 
notas = [] 
 
# Loop para entrada de notas 
while True: 
    entrada = input("Digite a nota do aluno (ou 'fim' para terminar): ") 
    if entrada.lower() == 'fim': 
        break 
    else: 
        try: 
            nota = float(entrada) 
            if 0 <= nota <= 10: 
                notas.append(nota) 
            else: 
                print("Nota inválida. Digite uma nota entre 0 e 10.") 
        except ValueError: 
            print("Entrada inválida. Digite um número ou 'fim' para terminar.") 
 
# Calculando a média das notas 
if len(notas) > 0: 
    media = sum(notas) / len(notas) 
else: 
    media = 0 
 
print(f"Média das notas: {media:.2f}") 
 
# Verificando se o aluno foi aprovado ou reprovado 
if media >= 6: 
    print("Aluno aprovado!") 
else: 
    print("Aluno reprovado.") 
 