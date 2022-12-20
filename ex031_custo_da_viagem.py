titulo = 'TRAVEL BUS'
print(f'{titulo:=^40}\n')

origem = str(input('Insira a origem: '))
destino = str(input('Insira o destido: '))
distancia = int(input('Insira a distância(Km) aproximada: '))

if distancia >= 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.5
print()
print('-' * 20)
print('ORIGEM: {}\nDESTINO: {}\nVALOR: R$ {:.2F}'.format(origem.capitalize(), destino.capitalize(), valor))
print('-' * 20)
