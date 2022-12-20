from time import sleep

titulo = 'PROGRESSÃO ARITMÉTICA'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contagem = 0
print('\nCalculando progressão...')
sleep(1)
while contagem < 10:
    print(f'{numero}', end=' ')
    contagem += 1
    numero += razao
print()
