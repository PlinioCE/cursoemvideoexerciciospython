titulo = 'Verifica Nome'
print(f'{titulo:=^40}\n')

nome = str(input('Digite o nome completo: ')).strip()
print('Verificando família Silva... ', 'SILVA' in nome.upper(), 'na posição:', nome.upper().find('SILVA') + 1)
