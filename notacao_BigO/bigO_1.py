"""
- NOTACAO BIG-O
    # Comparacao objetiva entre algoritmos
    # Considera diferencas entre poder de processamento, sistema operacional, liguagem de programacao
    # O quanto a 'complexidade'; do algoritmo aumenta de acordo com as entradas
"""
import timeit
# Funcao 1 - O(n)


def soma1(n):

    soma = 0
    for soma in range(n + 1):
        soma += 1

    return soma


t = timeit.Timer("soma1(10)", "from __main__ import soma1")
print(t.timeit())


def soma2(n):
    return (n * (n + 1)) / 2


t2 = timeit.Timer("soma2(10)", "from __main__ import soma2")
print(t2.timeit())
