titulo = 'LISTA DE PREÇOS'
print(f'{titulo:=^40}\n')

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>8.2f}')
print(f'\n{"FIM LISTA":=^40}')
