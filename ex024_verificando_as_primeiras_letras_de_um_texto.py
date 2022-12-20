titulo = 'Verifica Cidade'
print(f'{titulo:=^40}\n')

cidade = str(input('Digite o nome da cidade: ')).strip()
print('Buscando a primeira palavra São... ', cidade.upper() == 'SÃO')
