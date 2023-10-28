"""
Class functions
"""

from typing import Any


class classe_soma:
    def __call__(self, x,y):
        return x + y
    
print(classe_soma(2,2))