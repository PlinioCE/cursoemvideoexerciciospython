from datetime import date

titulo = 'VERIFICA MAIORIDADE'
print(f'{titulo:=^40}\n')

maiorIdade = 0
menorIdade = 0
anoAtual = date.today().year
for contagem in range(1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento da {contagem}ª pessoa: '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'\nPessoas MAIORES de 21 anos: {maiorIdade}'
      f'\nPessoas MENORES de 21 anos: {menorIdade}')
