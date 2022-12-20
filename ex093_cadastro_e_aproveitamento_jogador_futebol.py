titulo = 'APROVEITAMENTO JOGADOR'
print(f'{titulo:=^40}\n')

gols = []

nomeJogador = str(input('Nome do jogador: ')).strip().title()
partidasJogador = int(input(f'Quantas partidas do {nomeJogador}: '))
somaGols = 0
for g in range(1, partidasJogador + 1):
    gol = int(input(f'Quantidade de gols no {g}º jogo: '))
    gols.append(gol)
    somaGols += gol
print()
ficha = {'JOGADOR': nomeJogador, 'GOLS': gols, 'TOTAL DE GOLS': somaGols}
print(ficha)
print()
for k, v in ficha.items():
    print(f'{k}: {v}')
print()
print(f'{ficha["JOGADOR"]} participou de {len(ficha["GOLS"])} jogos.')
for g in range(1, len(ficha['GOLS']) + 1):
    if gols[g - 1] == 1:
        print(f'No {g}º jogo, marcou {gols[g - 1]} gol.')
    elif gols[g - 1] > 1:
        print(f'No {g}º jogo, marcou {gols[g - 1]} gols.')
    else:
        print(f'No {g}º jogo, não marcou gol.')
print(f'{nomeJogador} marcou um total de {somaGols} gols.')

# Resolução Curso em Vídeo

'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
