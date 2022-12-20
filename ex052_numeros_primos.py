titulo = 'NÚMEROS PRIMOS'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
resto = 0
for contagem in range(1, numero + 1):
    if numero % contagem == 0:
        resto += 1
if resto == 2:
    print(f'\n{numero} é um número PRIMO!')
else:
    print(f'\n{numero} NÃO é um número PRIMO!')

# Resolução Curso em Vídeo
''' num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c ==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '. format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!') '''
