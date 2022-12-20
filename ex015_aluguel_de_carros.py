titulo = ' LoCar '
print(f'{titulo:=^40}\n')

dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = int(input('Quantos quilômetros rodados? '))
valor_por_dia = dias_alugados * 60
valor_por_km = km_rodados * 0.15
valor_aluguel = valor_por_dia + valor_por_km
print(f'TOTAL: R$ {valor_aluguel:.2f}')
