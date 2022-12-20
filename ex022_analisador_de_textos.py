from time import sleep

titulo = 'ANALISADOR DE TEXTO'
print(f'{titulo:=^40}\n')

nome = str(input('Digite seu nome completo: ')).strip() # tira os espaços antes e depois da entrada de dados
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')

