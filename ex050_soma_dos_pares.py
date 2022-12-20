titulo = 'SOMA PARES'
print(f'{titulo:=^40}\n')

soma = 0
contador = 0
for contagem in range(1, 7):
    numero = int(input(f'Digite o {contagem}º número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'\nO resultado da soma dos {contador} números pares informados = {soma}.')
