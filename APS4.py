import random
import time
from IS import insertionSort
from QS import quicksort


def Qsort():
    any_numbers = random.sample(range(1, 1000), 42)

    already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,
                        32, 34, 39, 40, 42, 76, 87, 99, 112]

    inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
                50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

    repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]
    _name_ = "_main_"
    if _name_ == "_main_":
        test_cases = {'Números aleatórios': any_numbers,
                        'Já ordenados': already_sorted,
                        'Ordem inversa': inversed,
                        'Elementos repetidos': repeated
                    }
        print("***********")
        for name, lista in test_cases.items():
            print("\nCaso de teste: {}".format(name))
            print(lista)
            quicksort(lista)
            print("\n Ordenado:")
            print(lista)
        print("***********")


ini = time.time()
Qsort()
fim = time.time()
print("Tempo de Execução do QuickSort: ", fim-ini)

arr = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
                50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

ini_dois = time.time()
insertionSort(arr)
fim_dois = time.time()
print("Tempo de Execução do insertionSort ", fim_dois-ini_dois)
