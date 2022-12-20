from random import randint
from time import sleep

titulo = ' JOKENPÔ '
print(f'{titulo:=^40}')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogadaPc = randint(0, 2)
print('== LEGENDA =='
      '\n[0] - PEDRA'
      '\n[1] - PAPEL'
      '\n[2] - TESOURA')
jogador = int(input('\nEscolha sua jogada: '))
print('JO')
sleep(1/2)
print('KEN')
sleep(1/2)
print('PO...')
sleep(1/3)
print('-=' * 12)
print(f'Você jogou {itens[jogador]}'
      f'\nComputador jogou {itens[jogadaPc]}')
print('-=' * 12)
if jogador == 0:
    if jogadaPc == 0:
        resultado = 'EMPATE!'
    elif jogadaPc == 1:
        resultado = 'Computador VENCEU! PEDRA PERDE PARA PAPEL!'
    else:
        resultado = 'Você VENCEU! PEDRA GANHA DE TESOURA!'
elif jogador == 1:
    if jogadaPc == 0:
        resultado = 'Você VENCEU! PAPEL GANHA DE PEDRA!'
    elif jogadaPc == 1:
        resultado = 'EMPATE!'
    else:
        resultado = 'Computador VENCEU! PAPEL PERDE PARA TESOURA!'
elif jogador == 2:
    if jogadaPc == 0:
        resultado = 'Computador VENCEU! TESOURA PERDE PARA PEDRA!'
    elif jogadaPc == 1:
        resultado = 'Você VENCEU! TESOURA GANHA DE PAPEL!'
    else:
        resultado = 'EMPATE!'
else:
    resultado = 'JOGADA INVÁLIDA'
print()
print(resultado)
