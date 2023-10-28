from pdb import set_trace

def my_first_function():
    return 'something'

lambda: 'something'

class classFunction:
    def _call_():
        return 'something'
    

'''
Essas são as três formas de definir funções, a primeira forma, nomeando-a, a segunda anônima
e a terceira que não é bem uma função, através de classe e a utilização do dunder call.
'''

var = 2

def func():
    #print(var)
    var = 18
    print(var)
    set_trace()
func()
print(var)

#As variáveis declaradas dentro da função estão imersas no escopo da função - escopo local. Já as variáveis fora do escopo da função são variáveis globais.


