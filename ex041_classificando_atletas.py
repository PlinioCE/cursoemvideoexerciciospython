from datetime import date

titulo = 'CATEGORIAS NATAÇÃO'
print(f'{titulo:=^40}\n')

anoNascimento = int(input('Informe o ano de nascimento do(a) atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Idade atleta: {idade} anos'
      f'\nCategoria: {categoria}')
