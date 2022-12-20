titulo = 'MAIOR e MENOR'
print(f'{titulo:=^40}\n')

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

if numero1 > numero2:
    print(f'\nO número {numero1} é MAIOR que o número {numero2}.')
elif numero1 < numero2:
    print(f'\nO número {numero2} é MAIOR que o número {numero1}.')
else:
    print(f'\nO número {numero1} e o número {numero2} são IGUAIS!')
