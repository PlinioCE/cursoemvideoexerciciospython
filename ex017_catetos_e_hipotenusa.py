from math import sqrt, hypot

titulo = 'CalcTriRet'
print(f'{titulo:=^40}\n')

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
#hipotenusa = sqrt((catetoOposto ** 2) + pow(catetoAdjacente, 2))
area = (catetoOposto * catetoAdjacente) / 2

print('\nAs medidas do triângulo retângulo são:')
print('Cateto Op. = {}um \nCateto Ad. = {}um \nHipotenusa = {:.2f}um \nÁrea = {:.2}um²'.format(catetoOposto, catetoAdjacente, hipotenusa, area))
