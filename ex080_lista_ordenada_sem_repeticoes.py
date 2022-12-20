titulo = 'LISTA EM ORDEM'
print(f'{titulo:=^40}\n')

listagem = list()

for contador in range(0, 5):
    numero = int(input('Digite um número: '))
    if contador == 0 or numero > listagem[-1]:
        listagem.append(numero)
        print('Número adicionado no fim da lista!')
    else:
        posicao = 0
        while posicao < len(listagem):
            if numero <= listagem[posicao]:
                listagem.insert(posicao, numero)
                print(f'Número adicionado na posição {posicao} da lista.')
                break
            posicao += 1
print(f'\nOs valores digitados em ordem foram: {listagem}')
