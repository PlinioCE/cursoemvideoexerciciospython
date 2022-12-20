titulo = ' PAR OU ÍMPAR '
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
if numero % 2 == 0 and numero != 0:
    resultado = 'PAR'
elif numero == 0:
    resultado = 'NULO'
else:
    resultado = 'ÍMPAR'
print(f'O número {numero} é {resultado}.')
