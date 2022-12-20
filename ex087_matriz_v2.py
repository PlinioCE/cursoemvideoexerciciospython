titulo = 'MATRIZ 2'
print(f'{titulo:=^40}\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maiorNumeroLinha2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número da matriz na posição [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
for l in range(0, 3):
    coluna3 += matriz[l][2]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maiorNumeroLinha2:
        maiorNumeroLinha2 = matriz[1][c]
print()
print(f'A soma dos números PARES da matriz = {pares}.')
print(f'A soma dos números da 3ª coluna da matriz = {coluna3}.')
print(f'O MAIOR número da 2ª linha da matriz = {maiorNumeroLinha2}.')
