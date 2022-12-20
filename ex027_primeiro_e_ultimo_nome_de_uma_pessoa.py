titulo = 'Primeiro e Último Nome'
print(f'{titulo:=^40}\n')

nome = str(input('Digite seu nome completo: ')).strip()
print('Primeiro nome: {}.'.format(nome.split()[0]))
ultimo = (len(nome.split()))
print('Último nome: {}.'.format(nome.split()[ultimo - 1]))
