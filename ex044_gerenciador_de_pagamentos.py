titulo = 'CAIXA LOJA'
print(f'{titulo:=^40}\n')

valorProduto = float(input('Digite o valor da compra: R$ '))
print('\nFORMAS DE PAGAMENTO:'
      '\n[1] - À VISTA(DINHEIRO/ DÉBITO) - 10% desconto:'
      '\n[2] - À VISTA(CRÉDITO) - 5% desconto:'
      '\n[3] - CRÉDITO(2x s/ juros):'
      '\n[4] - CRÉDITO(10x) - 20% acréscimo:')
formaPagamento = int(input('\nEscolha a forma de pagamento: '))

if formaPagamento == 1:
      valorFinal = valorProduto - (valorProduto * 0.1)
      print(f'\nCOMPRA FINALIZADA'
            f'\nVALOR:     R$ {valorProduto:=6.2f}'
            f'\nDESCONTOS: R$ {valorProduto * 0.1:=7.2f}'
            f'\nTOTAL:     R$ {valorFinal:=7.2f}')
elif formaPagamento == 2:
      valorFinal = valorProduto - (valorProduto * 0.05)
      print(f'\nCOMPRA FINALIZADA'
            f'\nVALOR:     R$ {valorProduto:=6.2f}'
            f'\nDESCONTOS: R$ {valorProduto * 0.05:=7.2f}'
            f'\nTOTAL:     R$ {valorFinal:=7.2f}')
elif formaPagamento == 3:
      print(f'\nCOMPRA FINALIZADA'
            f'\nVALOR:         R$ {valorProduto:=6.2f}'
            f'\nPARCELAS:               2'
            f'\nVALOR PARCELA: R$ {valorProduto / 2:=7.2f}'
            f'\nDESCONTOS:     R$ {valorProduto * 0:=7.2f}'
            f'\nTOTAL:         R$ {valorProduto:=7.2f}')
elif formaPagamento == 4:
      valorFinal = valorProduto + (valorProduto * 0.2)
      quantidadeParcela = int(input('Informe a quantidade de parcelas: '))
      print(f'\nCOMPRA FINALIZADA'
            f'\nVALOR:         R$ {valorProduto:=6.2f}'
            f'\nPARCELAS: {quantidadeParcela:=15}'
            f'\nVALOR PARCELA: R$ {(valorFinal / quantidadeParcela):=7.2f}'
            f'\nACRÉSCIMO:     R$ {valorProduto * 0.2:=7.2f}'
            f'\nTOTAL:         R$ {valorFinal:=7.2f}')
else:
      print('\nFORMA DE PAGAMENTO INVÁLIDA!')
print('\nOBRIGADO E VOLTE SEMPRE!')
