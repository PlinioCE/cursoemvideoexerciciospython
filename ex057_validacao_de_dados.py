titulo = 'VALOR CORRETO'
print(f'{titulo:=^40}\n')

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('SEXO(M/F): ')).upper()[0].strip()
    if sexo != 'M' and sexo != 'F':
        print('\nVALOR INVÁLIDO.\nTENTE NOVAMENTE!')
        print()
    if sexo == 'M':
        sexoPessoa = 'MASCULINO'
    elif sexo == 'F':
        sexoPessoa = 'FEMININO'
print(f'\nSexo {sexoPessoa} registrado!')
print()

# Resolução Curso em Vídeo
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
