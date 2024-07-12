'''
Livro: Lógica de Programação para IA
Autor: Carlos Alberto Savi
Capítulo: A;goritmos Essenciais
'''

## Algoritmos de Ordenação 

# Bubble Sort 
def bubble_sort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
 
# Exemplo de uso 
arr = [64, 34, 25, 12, 22, 11, 90] 
bubble_sort(arr) 
print("Lista ordenada:", arr) 

# Selection Sort 
def selection_sort(arr): 
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
 
# Exemplo de uso 
arr = [64, 25, 12, 22, 11] 
selection_sort(arr) 
print("Lista ordenada:", arr)

# Insertion Sort 
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1 
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = key 
 
# Exemplo de uso 
arr = [12, 11, 13, 5, 6] 
insertion_sort(arr) 
print("Lista ordenada:", arr)

# Merge Sort
def merge_sort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
 
        merge_sort(L) 
        merge_sort(R) 
 
        i = j = k = 0 
 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i += 1 
            else: 
                arr[k] = R[j] 
                j += 1 
            k += 1 
 
        while i < len(L): 
            arr[k] = L[i] 
            i += 1 
            k += 1 
 
        while j < len(R): 
            arr[k] = R[j] 
            j += 1 
            k += 1 
 
# Exemplo de uso 
arr = [12, 11, 13, 5, 6, 7] 
merge_sort(arr) 
print("Lista ordenada:", arr) 

# Quick Sort
def partition(arr, low, high): 
    pivot = arr[high] 
    i = low - 1 
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1 
 
def quick_sort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high) 
        quick_sort(arr, low, pi - 1) 
        quick_sort(arr, pi + 1, high) 
 
# Exemplo de uso 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr, 0, n-1) 
print("Lista ordenada:", arr) 

## Algoritmos de Busca 

# Busca Linear
def busca_linear(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 
    return -1 
 
# Exemplo de uso 
arr = [2, 3, 4, 10, 40] 
x = 10 
resultado = busca_linear(arr, x) 
print("Elemento encontrado na posição:", resultado) 

# Busca Binária
def busca_binaria(arr, x): 
    low = 0 
    high = len(arr) - 1 
    mid = 0 
 
    while low <= high: 
        mid = (high + low) // 2 
        if arr[mid] < x: 
            low = mid + 1 
        elif arr[mid] > x: 
            high = mid - 1 
        else: 
            return mid 
    return -1 
 
# Exemplo de uso 
arr = [2, 3, 4, 10, 40] 
x = 10 
resultado = busca_binaria(arr, x) 
print("Elemento encontrado na posição:", resultado) 

## Recursão 

# Conceito de Recursão 

# Exemplo de uso de Recursão: Fatorial 
def fatorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * fatorial(n-1) 
 
# Exemplo de uso 
num = 5 
print("Fatorial de", num, "é", fatorial(num))

# Exemplo de uso de Recursão: Sequência de Fibonacci 
def fibonacci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
 
# Exemplo de uso 
num = 10 
for i in range(num): 
    print(fibonacci(i), end=" ")

# Exemplo de uso de Recursão: Problema das Torres de Hanói
def torres_de_hanoi(n, origem, destino, auxiliar): 
    if n == 1: 
        print(f"Mover disco 1 de {origem} para {destino}") 
        return 
    torres_de_hanoi(n-1, origem, auxiliar, destino) 
    print(f"Mover disco {n} de {origem} para {destino}") 
    torres_de_hanoi(n-1, auxiliar, destino, origem) 
 
# Exemplo de uso 
n = 3 
torres_de_hanoi(n, 'A', 'C', 'B') 
 
