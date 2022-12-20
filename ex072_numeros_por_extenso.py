titulo = 'NÚMEROS POR EXTENSO'
print(f'{titulo:=^40}\n')

numeroExt = ('zero', 'um', 'dois', 'três',
             'quatro', 'cinco', 'seis', 'sete',
             'oito', 'nove', 'dez', 'onze',
             'doze', 'treze', 'catorze', 'quinze',
             'dezesseis', 'dezesste', 'dezoito',
             'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numeroExt[numero]}.')
        print()
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print('\nPROGRAMA ENCERRADO!')

'''numero = -1
while numero not in range(0, 21):
    numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeroExt[numero]}.')'''
