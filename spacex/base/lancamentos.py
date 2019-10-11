from spacex.base.api import getx


def get_launches(method="", **query):
    """
        Retorna a lista de todos os lançamentos

    """
    return getx("launches", method, query)


def get_past_launches(**query):
    """
        Retorna a lista de todos os lançamentos passados

    """
    return getx("launches", "", query)


def get_latest_launch(**query):
    """
        Retorna informações do ultimo lançamento

    """
    return getx("launches", "latest", query)


def get_next_launch(**query):
    """
        Retorna informações do proximo lançamento

    """
    return getx("launches", "next", query)


def get_upcoming_launches(**query):
    """

        Retorna uma lista dos proximos lançamentos

    """
    return getx("launches", "upcoming", query)
