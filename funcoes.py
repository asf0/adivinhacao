from random import choice, shuffle
import pandas as pd
arq_csv = pd.read_csv('arq.csv', delimiter=',')
def msg_pos():
    pos = arq_csv['msg_positiva']
    return choice(pos)


def tema(num):
    temas_list = ['cidades', 'cores', 'nomes']
    tema = arq_csv[temas_list[num-1]]
    return choice(tema)


def diffop(opcao):
    difflist = [10, 5, 3]
    return difflist[opcao-1]


def embaralha(word):
    temp = list(word)
    shuffle(temp)
    return ''.join(temp)

if __name__ == '__main__':
    jogar()
