titulo = 'LISTA 5 VALORES'
print(f'{titulo:=^40}\n')

listagem = []
listaPosicaoMaior = []
listaPosicaoMenor = []
for lista in range(0, 5):
    listagem.append(int(input(f'Digite o número da posição {lista}: ')))
posicaoMaior = listagem.index(max(listagem))
for contador in range(0, listagem.count(max(listagem))):
    posicaoMaior = listagem.index(max(listagem), posicaoMaior)
    listaPosicaoMaior.append(posicaoMaior)
    posicaoMaior += 1
posicaoMenor = listagem.index(min(listagem))
for contador in range(0, listagem.count(min(listagem))):
    posicaoMenor = listagem.index(min(listagem), posicaoMenor)
    listaPosicaoMenor.append(posicaoMenor)
    posicaoMenor += 1
print(f'\nA lista foi preenchida com os seguintes valores: {listagem}')
if listagem.count(max(listagem)) == 1:
    print(f'O MAIOR valor da lista é {max(listagem)} e está na posição {listaPosicaoMaior}.')
else:
    print(f'O MAIOR valor da lista é {max(listagem)} e está nas posições {listaPosicaoMaior}.')
if listagem.count(min(listagem)) == 1:
    print(f'O MENOR valor da lista é {min(listagem)} e está na posição {listaPosicaoMenor}.')
else:
    print(f'O MENOR valor da lista é {min(listagem)} e está nas posições {listaPosicaoMenor}')

# Comentário YouTube Resolução Curso em Vídeo
'''lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')'''