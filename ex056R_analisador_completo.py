titulo = 'SELEÇÃO PESSOAS'
print(f'{titulo:=^40}\n')

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
homemVelho = ''
mulherMenor = 0
for contagem in range(1, 5):
    print(f'---------- {contagem}ª PESSOA ----------')
    nome = str(input(f'Nome: ')).strip().title()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip() # .upper() - ...and sexo == 'M'/'F'
    somaIdade += idade
    if idade > maiorIdadeHomem and sexo in 'Mm':
        maiorIdadeHomem = idade
        homemVelho = nome
    if idade < 20 and sexo in 'Ff':
        mulherMenor += 1
mediaIdade = somaIdade / contagem

print(f'\nSOMA IDADE: {somaIdade}'
      f'\nMÉDIA DAS IDADES: {mediaIdade}'
      f'\nHOMEM MAIS VELHO: {homemVelho}, {maiorIdadeHomem}'
      f'\nMULHERES ABAIXO DE 20: {mulherMenor}')
