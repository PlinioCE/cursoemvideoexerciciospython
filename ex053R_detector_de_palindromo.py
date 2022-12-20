titulo = 'PALÍNDROMO'
print(f'{titulo:=^40}\n')

frase = str(input('Escreva uma frase: ')).upper().strip()
separaFrase = frase.split()
juntaPalavras = ''.join(separaFrase)
inversoFrase = ''

for contagem in range(len(juntaPalavras) -1, -1, -1):
    inversoFrase += juntaPalavras[contagem]
print(f'\nORIGINAL:  {juntaPalavras}'
      f'\nINVERTIDA: {inversoFrase}')
if juntaPalavras == inversoFrase:
    print(f'\nA frase: {frase}. É PALÍNDROMO!')
else:
    print(f'A frase: {frase}. NÃO é PALÍNDROMO!')
