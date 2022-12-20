from datetime import date

titulo = 'ALISTAMENTO MILITAR'
print(f'{titulo:=^40}\n')

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
sexo = str(input('Informe o sexo [M/F]: ')).upper()

if sexo == 'M':
    if idade < 18:
        print(f'\nALISTAMENTO OBRIGATÓRIO de 1º/01/{anoNascimento + 18} até 30/04/{anoNascimento + 18}.')
    elif idade == 18:
        print(f'\nALISTAMENTO OBRIGATÓRIO de 1º/01/{anoAtual} até 30/04/{anoAtual}.')
    else:
        print(f'\nFORA DO PRAZO PARA ALISTAMENTO OBRIGATÓRIO DESDE 1º/05/{anoNascimento + 18}. '
          f'PROCURE UMA BASE MILITAR PARA REGULARIZAÇÃO.')
elif sexo == 'F':
    print('\nCIDADÃS BRASILEIRAS NÃO PRECISAM CUMPRIR O ALISTAMENTO OBRIGATÓRIO.')
else:
    print('\nVALOR PARA SEXO INVÁLIDO.')
