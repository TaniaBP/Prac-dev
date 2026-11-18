from src.operaciones import Operaciones

def test_sumar():
    op = Operaciones()
    # Verificamos que 2 + 3 sea igual a 5
    assert op.sumar(2, 3) == 5

def test_restar():
    op = Operaciones()
    # Verificamos que 3 - 2 sea igual a 1
    assert op.restar(3, 2) == 1

def test_sumar_negativos():
    op = Operaciones()
    # Probamos con números negativos para afinar la lógica
    assert op.sumar(-2, -3) == -5