from time import sleep

titulo = 'PROGRESSÃO ARITMÉTICA'
print(f'{titulo:=^40}\n')

numero = int(input('Digite um número: '))
razao = int(input('Informe a razão: '))
print('\nCalculando a progressão...')
sleep(1)
for contagem in range(0, 10):
    print(numero, end=' ')
    numero += razao
print()

# Resolução Curso em Vídeo
''' primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao)
    print('{} '.format(c), end='>> ')
print('ACABOU') '''
