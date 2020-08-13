import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1

        # Array de chars
        self.__valores = np.chararray(self.__capacidade, unicode=True)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    # Metodo publico
    def pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('Pilha cheia!')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('Pilha vazia!')
            return -1
        else:
            valor = self.__valores[self.__topo]
            self.__topo -= 1
            return valor

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


expressao = str(input('Digite uma expressao: '))
pilha = Pilha(len(expressao))

# c[d]
# a{b[c]d}e
# a{b(c]d}e
# a[b{c}d]e}
# a{b(c)

for i in range(len(expressao)):
    ch = expressao[i]
    if ch == '{' or ch == '[' or ch == '(':
        pilha.empilhar(ch)
    elif ch == '}' or ch == ']' or ch == ')':
        if not pilha.pilha_vazia():
            chx = str(pilha.desempilhar())
            if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
                print('Erro: ', ch, ' na posição ', i)
                break
        else:
            print('Erro: ', ch, ' na posição ', i)
if not pilha.pilha_vazia():
    print('Erro!')