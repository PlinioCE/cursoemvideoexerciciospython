from time import sleep

titulo = 'CALCULADORA'
print(f'{titulo:=^40}\n')
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

maiorNumero = 0
escolhaMenu = 0

while escolhaMenu != 5:
    print('======= MENU ======='
          '\n[1] - SOMAR'
          '\n[2] - MULTIPLICAR'
          '\n[3] - MAIOR NÚMERO'
          '\n[4] - NOVOS NÚMEROS'
          '\n[5] - SAIR'
          '\n====================')
    escolhaMenu = int(input('Escolha uma opção: '))
    print()
    if escolhaMenu == 1:
        soma = numero1 + numero2
        print(f'RESULTADO: {numero1} + {numero2} = {soma}')
    elif escolhaMenu == 2:
        multiplicacao = numero1 * numero2
        print(f'RESULTADO: {numero1} x {numero2} = {multiplicacao}')
    elif escolhaMenu == 3:
        if numero1 > numero2:
            print(f'RESULTADO: {numero1} > {numero2}')
        elif numero1 < numero2:
            print(f'RESULTADO: {numero1} < {numero2}')
        else:
            print(f'RESULTADO: {numero1} = {numero2}')
    elif escolhaMenu == 4:
        numero1 = int(input('Digite o 1º número: '))
        numero2 = int(input('Digite o 2º número: '))
    elif escolhaMenu == 5:
        print('ENCERRANDO PROGRAMA...')
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE...')
    sleep(1)
print()

# Resolução Curso em Vídeo
''' n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')
print('Fim do programa! Volte sempre!')'''
