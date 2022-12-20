titulo = 'CalcÁrea'
print(f'{titulo:=^40}\n')

comprimento = float(input('Insira o comprimento (m): '))
largura = float(input('Insira a largura (m): '))

area = comprimento * largura
tinta = area / 2

print('\nA área a ser pintada possui {:.2f} m² e serão \nnecessários {:.2f} l de tinta para pintá-la.'.format(area, tinta))
