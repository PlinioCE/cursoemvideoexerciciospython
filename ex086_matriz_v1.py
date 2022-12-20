titulo = 'MATRIZ'
print(f'{titulo:=^40}\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite o valor da matriz na posição [{l}, {c}]: ')))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
