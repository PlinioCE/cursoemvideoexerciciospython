titulo = 'FATORIAL - WHILE'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
fatorial = 1
contagem = numero
print()
print(f'{numero}! = ', end='')
while contagem > 0:
    print(f'{contagem}', end='')
    print(f' x ' if contagem > 1 else ' = ', end='')
    fatorial *= contagem
    contagem -= 1
print(f'{fatorial}')
