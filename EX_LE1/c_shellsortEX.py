import random
import time

def shellsort(arr):
    h = 1  # Inicializa a variável de incremento h com 1.
    n = len(arr)  # Obtém o comprimento do array.
    while h <= (n - 1)/3:
        h = 3 * h + 1  # Atualiza h para o próximo valor na sequência de incremento de Shell.
    while h > 0:  # Enquanto h for maior que 0, continue o processo de ordenação.
        for j in range(h, n):  # Itera sobre o array começando do índice h até o final.
            print(arr)  # Imprime o array atual para depuração.
            key = arr[j]  # Armazena o valor do elemento atual na variável key.
            i = j  # Inicializa a variável i com o valor de j.
            while i - h >= 0 and key <= arr[i - h]:  # Compara o key com o elemento que está h posições antes de i.
                arr[i] = arr[i - h]  # Move o elemento que está h posições antes de i para a posição atual.
                i -= h  # Decrementa i por h para continuar a comparação.
            arr[i] = key  # Insere o key na posição correta.
        h = (h - 1)//3  # Atualiza h para o próximo valor na sequência de incremento de Shell.


def generate_random_arr(size):
    return random.sample(range(size * 10), size)

def measure_func(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time


size_arr = 10
arr = generate_random_arr(size_arr)
time = measure_func(shellsort, arr)
print(arr)
print(f"Tempo de execução do Shellsort para {size_arr} elementos: {time:.5f} segundos")