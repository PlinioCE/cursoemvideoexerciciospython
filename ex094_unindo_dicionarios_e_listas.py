titulo = 'CADASTRO DE PESSOAS'
print(f'{titulo:=^40}\n')

pessoas = list()
mulheres = list()
somaIdade = contadorIdade = 0

while True:
    nome = str(input('NOME: ')).strip().title()
    sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    idade = int(input('IDADE: '))
    pessoa = {'NOME': nome, 'SEXO': sexo, 'IDADE': idade}
    pessoas.append(pessoa.copy())
    somaIdade += idade
    contadorIdade += 1
    mediaIdade = somaIdade / contadorIdade
    if sexo == 'F':
        mulheres.append(pessoa.copy())
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
    print()
print()
if len(pessoas) == 1:
    print(f'- Foi cadastrada {len(pessoas)} pessoa.')
else:
    print(f'- Foram cadastradas {len(pessoas)} pessoas.')
print(f'- A média de idade é de {mediaIdade:.1f} anos.')
if len(mulheres) == 1:
    print('- A mulher cadastrada foi, ', end='')
else:
    print('- As mulheres cadastradas foram, ', end='')
for m in mulheres:
    print(f'[{m["NOME"]}]', end=' ')
print()
print('- As pessoas com idade acima da média:')
for i in pessoas:
    if i['IDADE'] > mediaIdade:
        print(f'>>> NOME = {i["NOME"]}; SEXO = {i["SEXO"]}; IDADE = {i["IDADE"]}')
print()
print('FIM DO PROGRAMA')

# Resolução Curso em Vídeo

'''galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':  # ou if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():  # Possível erro com novo PyCharm
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< ENCERRADO >>')'''
