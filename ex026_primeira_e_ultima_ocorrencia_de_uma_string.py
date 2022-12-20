titulo = 'Busca Letra'
print(f'{titulo:=^40}\n')

frase = str(input('Digite uma frase: ')).strip()
print('A letra  A  aparece {}x na frase.'.format(frase.upper().count('A')))
print('A primeira letra  A  está na posição {}.'.format(frase.upper().find('A') + 1))
print('A última letra  A  está na posição {}.'.format(frase.upper().rfind('A') + 1))
