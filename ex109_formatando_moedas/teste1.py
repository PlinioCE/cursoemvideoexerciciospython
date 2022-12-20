from ex109_formatando_moedas import moeda1

numero = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda1.moeda(numero)} = {moeda1.metade(numero)}')
print(f'O dobro de {moeda1.moeda(numero)} = {moeda1.dobro(numero)}')
print(f'Aumentando em 10%, {moeda1.moeda(numero)} = {moeda1.aumentar(numero, 10)}')
print(f'Diminuindo em 13%, {moeda1.moeda(numero)} = {moeda1.diminuir(numero, 13)}')
