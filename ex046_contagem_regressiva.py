from time import sleep

titulo = 'VIRADA DE ANO'
print(f'{titulo:=^40}\n')

print('CONTAGEM REGRESSIVA...')
sleep(1)
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('\nFELIZ ANO NOVO!!!')
