from spacex.base import lancamentos


def x_proximo_lancamento():
    got_launch, _ = lancamentos.get_proximo_lancamento()
    return got_launch


def x_ultimo_lancamento():
    got_launch, _ = lancamentos.get_ultimo_lancamento()
    return got_launch


def x_proximos_lancamentos():
    got_launches, _ = lancamentos.get_proximos_lancamentos()
    return got_launches


def x_lancamentos_passados():
    got_launches, _ = lancamentos.get_lancamentos_passados()
    return got_launches


def test_get_proximo_lancamento():
    assert type(x_proximo_lancamento()) is dict


def test_get_ultimo_lancamento():
    assert type(x_ultimo_lancamento()) is dict


def test_get_proximos_lancamentos():
    assert type(x_proximos_lancamentos()) is list


def test_get_lancamentos_passados():
    assert type(x_lancamentos_passados()) is list
