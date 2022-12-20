from random import randint

titulo = 'LOTERIA'
print(f'{titulo:=^40}\n')

numeroSorteio = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram:', end=' ')
for numero in numeroSorteio:
    print(f'{numero}', end=' ')
print(f'\nO MAIOR valor sorteado foi: {sorted(numeroSorteio)[-1]}')
# print(f'O maior valor sorteado foi: {max(numeroSorteio)}')
print(f'O MENOR valor sorteado foi: {sorted(numeroSorteio)[0]}')
# print(f'O menor valor sorteado foi: {min(numeroSorteio)}')
