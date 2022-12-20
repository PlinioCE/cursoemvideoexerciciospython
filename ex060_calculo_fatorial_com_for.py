titulo = 'FATORIAL - FOR'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
fatorial = 1
print()
print(f'{numero}! = ', end='')
for numero in range(numero, 0, -1):
    print(f'{numero}', end='')
    print(f' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
print(fatorial)

# Resolução Curso em Vídeo
'''from math import factorial

numero = int(input('Digite um número: '))
fatorial = factorial(numero)
print(f'{numero}! = {fatorial}')'''
