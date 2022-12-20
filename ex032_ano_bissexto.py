from datetime import date

titulo = 'O ANO É BISSEXTO?'
print(f'{titulo:=^40}\n')

ano = int(input('Digite o ano que deseja verificar: '))

if ano == 0:
    ano = date.today().year #ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} é BISSEXTO!'.format(ano))
else:
    print('\nO ano {} NÃO é BISSEXTO!'.format(ano))
