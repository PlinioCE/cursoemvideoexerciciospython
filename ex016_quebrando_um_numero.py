from math import trunc

titulo = ' PARTE INTEIRA '
print(f'{titulo:=^40}\n')

numero = float(input('Digite um número real: '))
print(f'A parte inteira de {numero} é: {trunc(numero)}')
