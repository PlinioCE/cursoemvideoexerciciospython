from random import randint
from time import sleep

titulo = 'JOGO ADIVINHAÇÃO'
print(f'{titulo:=^40}\n')

numero = int(input('Escolha um número de 1 a 5: '))
numeroPC = randint(1, 5)
print('\nPRECESSANDO...')
sleep(3)

if numero == numeroPC:
    print('\nPARABÉNS! Você acertou o número adivinhão!')
else:
    print('\nSinto muito! O número era {}. Tente outra vez!'.format(numeroPC))
