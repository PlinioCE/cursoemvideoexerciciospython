from random import randint
from time import sleep

titulo = 'DADOS'
print(f'{titulo:=^30}\n')

jogador1 = randint(1, 6)
jogador2 = randint(1, 6)
jogador3 = randint(1, 6)
jogador4 = randint(1, 6)

jogo = {'Jogador 1': jogador1, 'Jogador 2': jogador2, 'Jogador 3': jogador3, 'Jogador 4': jogador4}
print('JOGANDO OS DADOS...')
sleep(2)
for k, v in jogo.items():
    print(f'O {k}, jogou {v}.')
    sleep(1)
print()
print(f'{" RANKING ":=^30}')
contador = 0
for j in sorted(jogo, key=jogo.get, reverse=True):
    contador += 1
    print(f'{contador}º lugar: {j} com {jogo[j]}')

# Resolução Curso em Vídeo

'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # itemgetter(1) - Utilizado (1) para ser ordenado pelo índice 1 da lista
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)'''
