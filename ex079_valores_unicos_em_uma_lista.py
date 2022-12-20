titulo = 'LISTA LIVRE'
print(f'{titulo:=^40}\n')

listagem = []
while True:
    listagem.append(int(input('Digite um número: ')))
    if listagem.count(listagem[-1]) > 1:
        listagem.pop()
        print('Número duplicado! NÃO ADICIONADO.')
    else:
        print('Número ADICIONADO com SUCESSO!')
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        print()
    if saida == 'N':
        break
print(f'{"-" * 40}')
listagem.sort()
if len(listagem) == 1:
    print(f'Foi incluído na lista apenas o número {listagem}.')
else:
    print(f'Foram incluídos na lista os números {listagem}.')

# Resolução Curso em Vídeo

'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}.')'''
