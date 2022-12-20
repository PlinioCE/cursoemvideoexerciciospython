from random import randint

titulo = 'PAR ou ÍMPAR'
print(f'{titulo:=^40}\n')

jogo = vencedor = resultado = ''
contador = 0

while vencedor != 'COMPUTADOR!':
    jogadaPc = randint(0, 10)
    print('PAR ou ÍMPAR')
    print('------------')
    jogador = str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).upper()
    numero = int(input('Escolha um número: '))
    somaNumeros = numero + jogadaPc
    if somaNumeros % 2 == 0:
        resultado = 'PAR'
    if somaNumeros % 2 == 1:
        resultado = 'ÍMPAR'
    if jogador in 'P' and resultado == 'PAR':
        vencedor = 'VOCÊ!'
    if jogador in 'ÍIM' and resultado == 'ÍMPAR':
        vencedor = 'VOCÊ!'
    if jogador in 'P' and resultado == 'ÍMPAR':
        vencedor = 'COMPUTADOR!'
    if jogador in 'ÍIM' and resultado == 'PAR':
        vencedor = 'COMPUTADOR!'
    print(f'\nVOCÊ: {numero}'
          f'\nCOMPUTADOR: {jogadaPc}'
          f'\nSOMA = {somaNumeros}'
          f'\nRESULTADO: {resultado}'
          f'\nVENCEDOR: {vencedor}')
    if vencedor == 'VOCÊ!':
        contador += 1
    print()
if contador == 1:
    print(f'GAME OVER! Você VENCEU apenas {contador} vez.')
elif contador > 1:
    print(f'GAME OVER! Você VENCEU {contador} vezes seguidas.')
else:
    print(f'GAME OVER! Você NÃO VENCEU nenhuma.')
print()

# Resolução Curso em Vídeo

'''from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'IÍ':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''
