'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Miniprojeto: Análise de Votação
'''

## Problema: Receber uma lista de votos (True e False) e determinar o resultado da votação: 

# Lista de votos: True para "Sim" e False para "Não" 
votos = [True, False, True, True, False, True, False, False, True, False] 

# Contagem de Votos
def contar_votos(votos): 
    votos_sim = 0 
    votos_nao = 0 
     
    for voto in votos: 
        if voto: 
            votos_sim += 1 
        else: 
            votos_nao += 1 
     
    return votos_sim, votos_nao 
 
 # Determinação do Resultado
def determinar_resultado(votos_sim, votos_nao): 
    if votos_sim > votos_nao: 
        return "Sim venceu" 
    elif votos_sim < votos_nao: 
        return "Não venceu" 
    else: 
        return "Houve empate" 

# Função Principal
def main(): 
    # Lista de votos 
    votos = [True, False, True, True, False, True, False, False, True, False] 
     
    # Contar votos 
    votos_sim, votos_nao = contar_votos(votos) 
     
    # Determinar resultado 
    resultado = determinar_resultado(votos_sim, votos_nao) 
     
    # Exibir resultado 
    print("Resultado da votação:", resultado) 
 
# Executar função principal 
main() 
