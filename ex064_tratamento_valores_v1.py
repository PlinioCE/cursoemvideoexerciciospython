titulo = 'ATÉ 9999'
print(f'{titulo:=^40}\n')

soma = contador = numero = 0

while numero != 9999:
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
print(f'\nQTD de NÚMEROS: {contador - 1}'
      f'\nSOMA dos NÚMEROS: {soma - 9999}')

# Resolução Curso em Vídeo
'''num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))'''
