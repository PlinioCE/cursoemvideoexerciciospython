titulo = 'MAIOR e MENOR de 3 NÚMEROS'
print(f'{titulo:=^40}\n')

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3ª número: '))

if numero1 < numero2 and numero1 < numero3:
    print('\nO menor número é {}.'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('\nO menor número é {}.'.format(numero2))
else:
    print('\nO menor número é {}.'.format(numero3))

if numero1 > numero2 and numero1 > numero3:
    print('O maior número é {}.'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é {}.'.format(numero2))
else:
    print('O maior número é {}.'.format(numero3))
