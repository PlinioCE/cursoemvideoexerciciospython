titulo = 'APROVEITAMENTO JOGADOR v2.0'
print(f'{titulo:=^40}\n')

gols = []
jogador = []
while True:
    nomeJogador = str(input('Nome do jogador: ')).strip().title()
    partidasJogador = int(input(f'Quantas partidas do {nomeJogador}: '))
    somaGols = 0
    for g in range(1, partidasJogador + 1):
        gol = int(input(f'Quantidade de gols no {g}º jogo: '))
        gols.append(gol)
        somaGols += gol
    fichaJogador = {'NOME': nomeJogador, 'JOGOS': partidasJogador, 'GOLS': gols.copy(), 'TOTAL DE GOLS': somaGols}
    jogador.append(fichaJogador.copy())
    gols.clear()
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
    print()
print()
print(f'{"CÓD.":<5}{"JOGADOR":<15}{"GOLS":<15}{"TOTAL"}')
for i, j in enumerate(jogador):
    print(f'{i:^5}{j["NOME"]:<15}{str(j["GOLS"]):<15}{j["TOTAL DE GOLS"]}')
print()
while True:
    detalhe = int(input('Informe o CÓD. do jogador para mais detalhes: '))
    print()
    if detalhe <= len(jogador) - 1:
        print(f'DETALHES DO JOGADOR {jogador[detalhe]["NOME"]}')
        contador = 1
        for g in jogador[detalhe]['GOLS']:
            print(f'No {contador}º jogo, marcou {g} gols.')
            contador += 1
    else:
        print('*** CÓD. não encontrado! ***')
    print()
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
    print()
print()
print('FIM DO PROGRAMA')

# Resolução Curso em Vídeo

'''time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')'''
