titulo = ' VOGAIS '
print(f'{titulo:=^40}\n')

palavras = (str(input('Digite a 1ª palavra: ')).strip().upper(),
            str(input('Digite a 2ª palavra: ')).strip().upper(),
            str(input('Digite a 3ª palavra: ')).strip().upper(),
            str(input('Digite a 4ª palavra: ')).strip().upper(),
            str(input('Digite a 5ª palavra: ')).strip().upper())

for palavra in palavras:
    print(f'\nA palavra {palavra} contém a(s) vogal(ais): ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
print()
