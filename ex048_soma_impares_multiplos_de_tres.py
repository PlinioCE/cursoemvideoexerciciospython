titulo = 'SOMA ÍMPARES de 1 a 500'
print(f'{titulo:=^40}\n')

soma = 0
contador = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        soma += contagem
        contador += 1
print(f'\nVALORES CONTABILIZADOS = {contador}'
      f'\nSOMA DOS VALORES = {soma}')
