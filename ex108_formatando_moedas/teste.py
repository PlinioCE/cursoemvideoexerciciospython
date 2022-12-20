from ex108_formatando_moedas import moeda

numero = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(numero)} = {moeda.moeda(moeda.metade(numero))}')
print(f'O dobro de {moeda.moeda(numero)} = {moeda.moeda(moeda.dobro(numero))}')
print(f'Aumentando em 10%, {moeda.moeda(numero)} = {moeda.moeda(moeda.aumentar(numero, 10))}')
print(f'Diminuindo em 13%, {moeda.moeda(numero)} = {moeda.moeda(moeda.diminuir(numero, 13))}')
