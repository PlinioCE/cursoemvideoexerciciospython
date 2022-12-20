import numbers

titulo = 'VAREJÃO TEM D TUDO'
print(f'{titulo:=^40}\n')

total = contador = produtoMaisBarato = produto1000 = 0
nomeProdutoMaisBarato = ' '

while True:
    produto = str(input('PRODUTO: ')).strip().title()
    preco = float(input('PREÇO: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        produto1000 += 1
    if contador == 1 or preco < produtoMaisBarato:
        produtoMaisBarato = preco
        nomeProdutoMaisBarato = produto
    saida = ' '
    while saida not in 'SN':
        print('=========================================')
        saida = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('=========================================')
    if saida == 'N':
        break
print('============ FIM DO PROGRAMA ============')
print('=========================================')
print(f'VALOR TOTAL DA COMPRA: \033[7mR$ {total:.2f}\033[m')
print(f'PRODUTO > R$ 1000.00: \033[7m0{produto1000} produto(s)\033[m')
print(f'PRODUTO + BARATO: \033[7m{nomeProdutoMaisBarato}, por R$ {produtoMaisBarato:.2f}\033[m')
print('=========================================')
print('OBRIGADO E VOLTE SEMPRE!')
