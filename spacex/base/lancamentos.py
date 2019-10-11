from spacex.base.api import getx

def get_proximo_lancamento():
    """
        Retorna informações do proximo lançamento

    """
    return getx("launches", "next")


def get_ultimo_lancamento():
    """
        Retorna informações do ultimo lançamento

    """
    return getx("launches", "latest")


def get_proximos_lancamentos():
    """

        Retorna uma lista dos proximos lançamentos

    """
    return getx("launches", "upcoming")


def get_lancamentos_passados():
    """
        Retorna a lista de todos os lançamentos passados

    """
    return getx("launches", "past")
