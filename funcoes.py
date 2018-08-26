from random import choice, shuffle
import csv
from collections import defaultdict

col = defaultdict(list)

with open("arq.csv") as File:
    reader = csv.DictReader(File)
    for c in reader:
        for(x, y) in c.items():
            col[x].append(y)
File.close()

def msg_pos():
    pos = col['msg_positiva']
    return choice(pos)


def tema(num):
    temas_list = ['cidades', 'cores', 'nomes']
    tema = col[temas_list[num-1]]
    return choice(tema)


def diffop(opcao):
    difflist = [10, 5, 3]
    return difflist[opcao-1]


def embaralha(word):
    temp = list(word)
    shuffle(temp)
    return ''.join(temp)

