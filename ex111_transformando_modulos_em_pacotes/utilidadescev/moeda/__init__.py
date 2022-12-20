def metade(n=0, formato=False):
    """
    -> Calcula a metade do número.
    :param n: Número fornecido pelo usuário;
    :return: A metade do número.
    """
    r = n / 2
    return r if formato is False else moeda(r)


def dobro(n=0, formato=False):
    """
    -> Calcula o dobro do número.
    :param n: Número fornecido pelo usuário;
    :return: O dobro do número.
    """
    r = n * 2
    return r if not formato else moeda(r)


def aumentar(n=0, p=0, formato=False):
    """
    -> Calucula e soma a porcentagem de um número.
    :param n: Número fornecido pelo usuário;
    :param p: Porcentagem predefinida na programação;
    :return: Número somado da porcentagem predefinida.
    """
    r = n + (n * p / 100)
    if not formato:
        return r
    else:
        return moeda(r)


def diminuir(n=0, p=0, formato=False):
    """
    -> Calucula e subtrai a porcentagem de um número.
    :param n: Número fornecido pelo usuário;
    :param p: Porcentagem predefinida na programação;
    :return: Número subtraído da porcentagem predefinida.
    """
    r = n - (n * p / 100)
    return r if not formato else moeda(r)


def moeda(n=0, m='R$'):
    return f'{m} {n:>.2f}'.replace('.', ',')


def resumo(n=0, an=0, dn=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metado do preço: \t{metade(n, True)}')
    print(f'Aumentando {an}%: \t{aumentar(n, an, True)}')
    print(f'Diminuindo {dn}%: \t{diminuir(n, dn, True)}')
    print('-' * 30)
