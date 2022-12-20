titulo = ' TSE '
print(f'{titulo:=^40}')


def voto(i=0):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - i
    if 65 >= idade >= 18:
        situacao = f'Com {idade} anos em {ano_atual}, o voto é OBRIGATÓRIO.'
    elif 16 <= idade < 18 or i > 65:
        situacao = f'Com {idade} anos em {ano_atual}, o voto é OPCIONAL.'
    else:
        situacao = f'Com {idade} anos em {ano_atual}, NÃO VOTA.'
    return situacao


ano_nascimento = int(input('Informe o ano de nascimento: '))
print()
print(voto(ano_nascimento))
