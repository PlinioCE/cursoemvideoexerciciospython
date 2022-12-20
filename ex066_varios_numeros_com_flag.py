titulo = 'LER NÚMEROS'
print(f'{titulo:=^40}\n')

contador = soma = 0

while True:
    numero = int(input('Digite um número (9999 para sair): '))
    if numero == 9999:
        break
    contador += 1
    soma += numero
print(f'\nA soma dos {contador} números = {soma}.')
