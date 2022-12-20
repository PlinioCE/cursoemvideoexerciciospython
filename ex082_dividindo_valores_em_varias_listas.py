titulo = 'CRIA LISTAS'
print(f'{titulo:=^40}\n')

listagem = []
while True:
    listagem.append(int(input('Digite um número: ')))
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
listaPar = []
listaImpar = []
for numero in listagem:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(f'\nA lista PRINCIPAL é: {listagem}')
print(f'A lista de PARES é: {listaPar}')
print(f'A lista de ÍMPARES é: {listaImpar}')

# Resolução Curso em Vídeo

'''num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''
