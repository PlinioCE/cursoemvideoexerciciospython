titulo = 'Ficha Jogador'
print(f'{titulo:=^40}\n')


def ficha(j='', g=''):
    """
    -> Função informa quantos gols um determinado jogador fez.
    :param j: Nome do jogador;
    :param g: Número de gols do jogador;
    :return: sem retorno
    """
    if j == '':
        j = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = '0'
    print(f'O jogador {j} marcou {g} gol(s) no campeonato.')


nomeJogador = str(input('Nome do jogador: ')).strip().title()
golsJogador = str(input('Número de gols: ')).strip()
print()
ficha(nomeJogador, golsJogador)

# Resolução Curso em Vídeo


'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} no campeonato.')
    
    
# Programa Principa
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=0)
else:
    ficha(n, g)'''
