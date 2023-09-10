"""
Anotações de tipo
"""

"""HOFs"""
from numbers import Number
from typing import Any, Callable


def soma (x:Number, y:Number) -> Number:
    return x + y

soma_2 = lambda val: val + 2
def reaplica(func: Callable, val: Any) -> Any:
    return func(
        func(val)
    )
    """Função que reaplica a função ao resultado da chamada."""

def seleciona(op: str) -> Callable:
    """Seleciona uma função usando seu nome."""
    ops ={
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
    }
    return ops[op]