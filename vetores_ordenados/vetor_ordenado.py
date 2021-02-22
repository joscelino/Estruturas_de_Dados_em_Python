"""
https://www.cs.usfca.edu/~galles/visualization/Search.html
"""

import numpy as np


class VetorOrdenado:

    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida!')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    # O(log n)
    def pesquisar_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_superior + limite_inferior) / 2)
            # Se achou na primeria tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se nao achou o valor na primeira tentativa
            elif limite_inferior > limite_superior:
                return -1
            # Dividindo os elementos
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    # O(n)
    def excluir(self, valor) -> int:
        """ Exclui valor do vetor, caso exista """
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1

        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


if __name__ == '__main__':

    vetor = VetorOrdenado(5)
    vetor.imprime()
    vetor.insere(6)
    vetor.insere(4)
    vetor.insere(7)
    vetor.insere(5)
    vetor.insere(1)
    vetor.excluir(7)
    vetor.excluir(4)
    print(vetor.pesquisa_linear(9))
    print(vetor.excluir(9))
    vetor.imprime()

    print(vetor.pesquisar_binaria(6))