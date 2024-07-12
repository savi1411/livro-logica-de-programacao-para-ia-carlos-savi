'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Miniprojeto: Análise de Dados de Vendas
'''

# Problema:
# Desenvolver um sistema que analise os dados de vendas de uma empresa, 
# ordene os dados por valor de venda, busque informações específicas 
# e calcule métricas como o total de vendas e a média de vendas. 

## Solução passo a passo

# Passo 1: Representação dos Dados 

# Lista de vendas 
vendas = [ 
    {"produto": "Produto A", "quantidade": 10, "valor": 100.0}, 
    {"produto": "Produto B", "quantidade": 5, "valor": 200.0}, 
    {"produto": "Produto C", "quantidade": 2, "valor": 50.0}, 
    {"produto": "Produto D", "quantidade": 7, "valor": 300.0}, 
    {"produto": "Produto E", "quantidade": 1, "valor": 500.0} 
] 

# Passo 2: Ordenação dos Dados 

# Implementação do Bubble Sort 
def bubble_sort(vendas): 
    n = len(vendas) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if vendas[j]["valor"] > vendas[j+1]["valor"]: 
                vendas[j], vendas[j+1] = vendas[j+1], vendas[j] 
 
# Ordenar as vendas 
bubble_sort(vendas) 
print("Vendas ordenadas por valor:") 
for venda in vendas: 
    print(venda)  

# Passo 3: Busca de Informações 

# Implementação da Busca Linear 
def busca_venda(vendas, nome_produto): 
    for venda in vendas: 
        if venda["produto"] == nome_produto: 
            return venda 
    return None 
 
# Buscar uma venda específica 
produto_procurado = "Produto D" 
venda_encontrada = busca_venda(vendas, produto_procurado) 
print(f"Venda encontrada: {venda_encontrada}") 

# Passo 4: Cálculo de Métricas 

# Função para calcular o total de vendas 
def calcular_total_vendas(vendas): 
    total = 0 
    for venda in vendas: 
        total += venda["valor"] * venda["quantidade"] 
    return total 
 
# Função para calcular a média de vendas 
def calcular_media_vendas(vendas): 
    total = calcular_total_vendas(vendas) 
    quantidade_total = sum(venda["quantidade"] for venda in vendas) 
    return total / quantidade_total 
 
# Calcular e imprimir as métricas 
total_vendas = calcular_total_vendas(vendas) 
media_vendas = calcular_media_vendas(vendas) 
print(f"Total de vendas: {total_vendas}") 
print(f"Média de vendas: {media_vendas:.2f}")

 