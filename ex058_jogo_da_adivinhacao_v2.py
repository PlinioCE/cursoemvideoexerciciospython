from random import randint

titulo = 'JOGO ADIVINHAÇÃO - WHILE'
print(f'{titulo:=^40}\n')

numeroJogador = 0
numeroPc = randint(1, 10)
restart = ''
contador = 0

while numeroJogador != numeroPc or restart != 'N':
    numeroJogador = int(input('Escolha um número de 1 a 10: '))
    contador += 1
    if numeroJogador < numeroPc:
        print('MAIS! Tente de novo...')
        print()
    elif numeroJogador > numeroPc:
        print('MENOS! Tente de novo...')
        print()
    elif numeroJogador == numeroPc:
        print('PARABÉNS! ACERTOU EM CHEIO!')
        print(f'\nForam necessárias {contador} tentativas para o acerto!')
        restart = str(input('\nDeseja jogar novamente? [S/N] ')).upper()
        print()
print()

# Resolução Curso em Vídeo
# from randon import randint
'''computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...  Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''
