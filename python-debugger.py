import pdb
from testing import validate

nome = 'Luca'
age = 22
mouse = 'deathadder'


def soma(x:int,y:int)-> int:
    return validate(x,y)

def divi(x,y):
    return x / y

try:
    divi(2,0)
except Exception:
    from sys import exc_info
    pdb.post_mortem(exc_info())

#step
#next
#list
#where
