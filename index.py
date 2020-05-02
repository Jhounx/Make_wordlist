import os 
from itertools import product

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

ar = []
a = 's'
while(a != ''):
    a = str(input('>>'))
    ar.append(a)

xs = int(input('Quantidade de junções: '))
permsList = remove_repetidos([''.join(x) for x in product(ar, repeat=xs)])
arquive_name = str(input('Nome do arquivo: '))

with open(arquive_name, 'w') as nha: 
    for x in permsList:
        nha.write(x + "\n")

print('Lista Criada com sucesso!')
