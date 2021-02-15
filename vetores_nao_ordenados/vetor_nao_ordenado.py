import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self) -> None:
        """ Verifica e imprime a quantidade de elementos no vetor """
        if self.ultima_posicao == -1:
            print('Vetor vazio!')
        else:
            for i in range(self.ultima_posicao +1):
                print(i, ' - ', self.valores[i])

    # O(1) - O(2)
    def insere(self, valor) -> None:
        """ Verifica a capacidade do vetor e insere um novo valor se houver espaco"""
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atingida!')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor) -> int:
        """ Efetua pesquisa linear de valores no vetor """
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    # O(n)
    def excluir(self, valor) -> int:
        """ Exclui valor do vetor, caso exista """
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

if __name__ == '__main__':

    vetor = VetorNaoOrdenado(4)
    vetor.imprime()
    vetor.insere(4)
    vetor.insere(3)
    vetor.insere(7)
    vetor.insere(8)
    vetor.insere(9)
    vetor.imprime()
    print(vetor.pesquisar(3))
    vetor.excluir(8)
    print(vetor.excluir(0))
    vetor.imprime()