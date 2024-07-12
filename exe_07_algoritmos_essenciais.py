'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: Algoritmos Essenciais
Soluções dos Exercícios
'''

## Exercício 2 

# Considere o seguinte código de Busca Binária. 
# Qual será a saída do código ao procurar 
# o número 10 na lista [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]? 
def busca_binaria(arr, x): 
    low = 0 
    high = len(arr) - 1 
    while low <= high: 
        mid = (high + low) // 2 
        if arr[mid] < x: 
            low = mid + 1 
        elif arr[mid] > x: 
            high = mid - 1 
        else: 
            return mid 
    return -1 
 
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
x = 10 
resultado = busca_binaria(arr, x) 
print("Resultado da busca:", resultado) 
 

# Saída Esperada: 
# O código de Busca Binária retorna -1, 
# indicando que o número 10 não está na lista. 

## Exercício 3

# Utilizando com referência o exemplo prático apresentado na parte teórica, 
# implemente o algoritmo de ordenação Bubble Sort 
# para ordenar uma lista de números inteiros em ordem crescente. 
# Escreva um código que receba uma lista e a ordene usando o Bubble Sort. 
# Teste seu código com a lista [45, 23, 89, 77, 12, 67, 34]. 

# Implementação do Bubble Sort 
def bubble_sort(lista): 
    n = len(lista) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if lista[j] > lista[j+1]: 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
 
# Lista para ordenar 
lista = [45, 23, 89, 77, 12, 67, 34] 
bubble_sort(lista) 
print("Lista ordenada:", lista) 

# Saída Esperada: 
# Lista ordenada: [12, 23, 34, 45, 67, 77, 89] 

 