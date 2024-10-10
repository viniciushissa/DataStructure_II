import random
import time

def heap_down(arr, n, i):
    # Inicializa o maior elemento como o índice atual
    largest = i
    # Calcula o índice do filho esquerdo
    left = 2 * i + 1
    # Calcula o índice do filho direito
    right = 2 * i + 2

    # Se o filho esquerdo é maior que o nó atual, atualiza o maior
    if left < n and arr[i] < arr[left]:
        largest = left

    # Se o filho direito é maior que o maior valor encontrado, atualiza o maior
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Se o maior valor não é o nó atual, troca e aplica a função recursivamente no filho afetado
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap_down(arr, n, largest)

def build_heap(arr, n):
    # Constrói o heap a partir do array, começando do último nó não folha para o início
    for i in range(n // 2 - 1, -1, -1):
        heap_down(arr, n, i)

def heapsort(arr):
    # Obtém o tamanho do array
    n = len(arr)

    # Constrói o heap usando o array
    build_heap(arr, n)

    # Extrai elementos um a um do heap e constrói a ordenação
    for i in range(n - 1, 0, -1):
        # Move o elemento atual (raiz do heap) para o final do array
        arr[i], arr[0] = arr[0], arr[i]
        # Reconstroi o heap com o tamanho reduzido
        heap_down(arr, i, 0)


def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
print(arr)
time = measure_func(heapsort, arr)
print(arr)
print(f"Tempo de execução do Heapsort para {size_arr} elementos: {time:.5f} segundos")