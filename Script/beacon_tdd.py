
def beacon_tdd(n):
    assert isinstance(n, int)
    if n % 3 == 0 and n % 5 == 0:
        return 'Sucesso'
    if n % 3 == 0:
        return 'Sucesso'
    if n % 5 == 0:
        return 'Sucesso'
    return 'Falha'