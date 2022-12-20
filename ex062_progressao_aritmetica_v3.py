from time import sleep

titulo = 'PROGRESSÃO ARITMÉTICA'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

contagem = 0
acrescimo = 10
total = 0
print('\nCalculando progressão...')
sleep(1)

while acrescimo != 0:
    total = total + acrescimo
    while contagem < total:
        print(f'{numero}', end=' ')
        contagem += 1
        numero += razao
    acrescimo = int(input('\nDeseja exibir mais quantos termos? '))
print(f'\nForam exibidos um total de {total} termos.')
