titulo = 'PESO DE 5'
print(f'{titulo:=^40}\n')

maiorPeso = 0
menorPeso = 99999
for contagem in range(1, 6):
    peso = float(input(f'Informe o peso(Kg) da {contagem}ª pessoa: '))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < maiorPeso and peso < menorPeso:
        menorPeso = peso
print(f'\nA pessoa MAIS pesada tem {maiorPeso:.1f}Kg'
      f'\nA pessoa MENOS pesada tem {menorPeso:.1f}Kg')

# --------------------------------------------------------------------------------------------------
# Resolução Curso em Vídeo
'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: ').format(p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if pesp < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg.'.format(maior))
print('O menor peso lido foi de {:.1f}Kg.'.format(menor))'''
