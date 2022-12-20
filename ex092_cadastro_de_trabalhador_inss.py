from datetime import date

titulo = 'Cálculo INSS'
print(f'{titulo:=^40}\n')

anoAtual = date.today().year
nome = str(input('Nome: ')).strip().title()
anoNascimento = int(input('Ano Nascimento: '))
idade = anoAtual - anoNascimento
ctps = int(input('Nº CTPS: '))
if ctps != 0:
    anoContratacao = int(input('Ano Contratação: '))
    aposentadoria = idade + ((anoContratacao + 35) - anoAtual)
    salario = float(input('Salário: R$ '))
    dados = {'NOME': nome, 'IDADE': idade, 'CTPS': ctps, 'CONTRATAÇÃO': anoContratacao, 'SALÁRIO': salario, 'APOSENTADORIA': aposentadoria}
else:
    dados = {'NOME': nome, 'IDADE': idade, 'CTPS': ctps}
print()
for k, v in dados.items():
    print(f'{k}: {v}')

# Resolução Curso em Vídeo

'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['aposentadoria'] = dados[idade] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    {k} tem o valor {v}')'''
