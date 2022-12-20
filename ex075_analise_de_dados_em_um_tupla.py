titulo = 'ARMAZENA NÚMEROS'
print(f'{titulo:=^40}\n')

numeros = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: ')))

print(f'\nForam digitados {numeros}.')
if numeros.count(9) == 1:
    print(f'O número 9 apareceu {numeros.count(9)} vez.')
elif numeros.count(9) > 1:
    print(f'O número 9 apareceu {numeros.count(9)} vezes.')
else:
    print('O número 9 NÃO foi digitado.')
if numeros.count(3) > 0:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 NÃO foi digitado.')
print('Os números PARES:', end=' ')
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
print()
