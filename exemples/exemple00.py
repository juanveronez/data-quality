def soma(x: int, y: int) -> int:
    """
    Exemplo de validação "na mão", é possível fazer, mas se torna trabalhoso e escala sua complexidade
    """
    assert isinstance(x, int)
    assert isinstance(y, int)
    
    return x + y
