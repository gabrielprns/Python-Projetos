def insertionSort(arr):
    # função para ordenar uma sequência de números

    for i in range(1, len(arr)):

        key = arr[i]
        # será criada uma váriavel para cada item da lista
        j = i - 1
        # váriavel para trocar o item da lista de posição
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            # enquanto a váriavel de troca tiver um valor positivo e a variável key for menor que a váriavel de troca armazenada na lista, j por ter um valor superior a key avançará uma posição
            j -= 1
            # quebra do laço
        arr[j + 1] = key
        # a ordem original dos valores representados por i será subistítuida pela nova ordem dos valores representados por j

def prin():
    arr = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
                50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]
    # Lista criada

    # essa instrução irá adicionar na lista os números digitados anteriormente
    insertionSort(arr)
    # essa função será chamada
    print("A lista ficará assim:")
    for i in range(len(arr)):
        print("%d" % arr[i])
    # dentro dessa estrutura de repetição serão impressos todos os número armazenados na lista arr

prin()
