titulo = 'SOMA DIGITADOS'
print(f'{titulo:=^40}\n')

soma = somaQuantidade = media = maiorNumero = menorNumero = contagem = 0
saida = 'S'

while saida in 'S':
    contagem += 1
    quantidadeNumeros = int(input('Quantos números deseja somar? '))
    somaQuantidade += quantidadeNumeros
    contador = 0
    while contador < quantidadeNumeros:
        numero = int(input('Digite um número: '))
        contador += 1
        soma += numero
        if contador == 1:
            menorNumero = maiorNumero = numero
        else:
            if numero > maiorNumero:
                maiorNumero = numero
            if numero < menorNumero:
                menorNumero = numero
    saida = str(input('\nDeseja acrescentar mais números? [S/N] ')).upper()
    media = soma / somaQuantidade
print(f'\nSOMA = {soma}'
      f'\nMÉDIA = {media:.1f}'
      f'\nMAIOR = {maiorNumero}'
      f'\nMENOR = {menorNumero}')
