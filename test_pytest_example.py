import mi_modulo

def test_sum():
    assert mi_modulo.sum([1, 2, 3]) == 6, "Debería ser 6"

def test_sum_tuple():
    assert mi_modulo.sum((1, 2, 2)) == 6, "Debería ser 6"
