titulo = 'LISTAS PARES e ÍMPARES'
print(f'{titulo:=^40}\n')

listaTodos = [[], []]

for contagem in range(0, 7):
    numero = int(input(f'Digite o {contagem + 1}º número: '))
    if numero % 2 == 0:
        listaTodos[0].append(numero)
    elif numero % 2 == 1:
        listaTodos[1].append(numero)
listaTodos[0].sort()
listaTodos[1].sort()
#print(f'\nA lista completa é: {listaTodos}.')
print(f'\nA lista de pares é: {listaTodos[0]}')
print(f'A lista de ímpares é: {listaTodos[1]}')
