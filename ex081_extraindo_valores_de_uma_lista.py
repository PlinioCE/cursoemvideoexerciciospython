tiutlo = 'RECEBE VALORES'
print(f'{tiutlo:=^40}\n')

listagem = []
while True:
    listagem.append(int(input('Digite um número: ')))
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if saida == 'N':
        break
    print()
if len(listagem) == 1:
    print(f'\nFoi adicionado {len(listagem)} número à lista.')
elif len(listagem) > 1:
    print(f'\nForam adicionados {len(listagem)} números à lista.')
listagem.sort(reverse=True)
print(f'A lista em ordem decrescente: {listagem}')
if listagem.count(5) == 1:
    print(f'O número 5 foi adicionado {listagem.count(5)} vez.')
elif listagem.count(5) > 1:
    print(f'O número 5 foi adicionado {listagem.count(5)} vezes.')
else:
    print('O número 5 NÃO foi adicionado à lista.')
