def insertionSort(arr):
    # função para ordenar uma sequência de números
    for i in range(1, len(arr)):

        key = arr[i]
        # será criada uma váriavel para cada item da lista
        j = i - 1
        # váriavel para trocar o item da lista de posição
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            #enquanto a váriavel de troca tiver um valor positivo e a variável key for menor que a váriavel de troca armazenada na lista, j por ter um valor superior a key avançará uma posição
            j -= 1
            #quebra do laço
        arr[j + 1] = key
        #a ordem original dos valores representados por i será subistítuida pela nova ordem dos valores representados por j


arr = []
# Lista criada
for c in range(1, 21):
    # estrutura de repetição criada para serem adicionados vários números na lista
    c = int(input("Digite um número:"))
    # o usuário irá digitar números a serem adicionados na lista
    arr.append(c)
# essa instrução irá adicionar na lista os números digitados anteriormente
insertionSort(arr)
# essa função será chamada
print("A lista ficará assim:")
for i in range(len(arr)):
    print("%d" % arr[i])
# dentro dessa estrutura de repetição serão impressos todos os número armazenados na lista arr
