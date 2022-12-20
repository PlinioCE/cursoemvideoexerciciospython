titulo = str('CalConversion')
print(f'{titulo:=^40} \n')

m = float(input('Digite o valor, em metros, a ser convertido: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('\n{} m equivale ~ {:.2f} km.'.format(m, km))
print('{} m equivale ~ {:.2f} hm.'.format(m, hm))
print('{} m equivale a {:.2f} dam.'.format(m, dam))
print('{} m equivale a {:.0f} dm.'.format(m, dm))
print('{} m equivale a {:.0f} cm.'.format(m, cm))
print('{} m equivale a {:.0f} mm.'.format(m, mm))
