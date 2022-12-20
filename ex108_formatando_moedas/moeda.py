def metade(n=0):
    """
    -> Calcula a metade do número.
    :param n: Número fornecido pelo usuário;
    :return: A metade do número.
    """
    r = n / 2
    return r


def dobro(n=0):
    """
    -> Calcula o dobro do número.
    :param n: Número fornecido pelo usuário;
    :return: O dobro do número.
    """
    r = n * 2
    return r


def aumentar(n=0, p=0):
    """
    -> Calucula e soma a porcentagem de um número.
    :param n: Número fornecido pelo usuário;
    :param p: Porcentagem predefinida na programação;
    :return: Número somado da porcentagem predefinida.
    """
    r = n + (n * p / 100)
    return r


def diminuir(n=0, p=0):
    """
    -> Calucula e subtrai a porcentagem de um número.
    :param n: Número fornecido pelo usuário;
    :param p: Porcentagem predefinida na programação;
    :return: Número subtraído da porcentagem predefinida.
    """
    r = n - (n * p / 100)
    return r


def moeda(n=0, m='R$'):
    return f'{m} {n:>.2f}'.replace('.', ',')
