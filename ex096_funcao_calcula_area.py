titulo = ' Função Área '
print(f'{titulo:=^40}\n')


def calc_area(largura, comprimento):
    area = largura * comprimento
    print(f'A área {largura}m x {comprimento}m = {area:.2f}m².')


largura1 = float(input('Informe a largura(m): '))
comprimento1 = float(input('Informe o comprimento(m): '))
print()
calc_area(largura1, comprimento1)
