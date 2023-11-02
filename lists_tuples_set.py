#Lists,tuples and sets

"""
Listas são objetos utilizados para guardar vários elementos do mesmo tipo de dado
ou de um tipo de dado diferente. Para criar uma lista você pode utilizar os colchetes
[].
"""
objetos = ['bola','borracha','lápis','mesa']
print(objetos)
objetos.append('lâmpada')
print(objetos)

"""
Os itens da lista são acessáveis utilizando os colchetes e dentro deles o índice do elemento.
Além disso, listas possuem seus métodos e propriedades. Listas e outros objetos de coleção 
em Python utilizam o índice 0, logo, o primeiro elemento possui índice 0.
Dessa forma:
H E L L O
0 1 2 3 4  
"""

print(objetos[0]) # bola

"""
E também, é possível acessar o último elemento utilizando o sinal de -
H  E  L  L  O
-5 -4 -3 -2 -1
"""
print('Hello'[-5]) # H


"""
Listas também permitem o slicing, você pode pegar as fatias de uma lista utilizando a seguinte sintaxe:
lista[a:b] sabendo que a é onde começa e é incluido e b é até onde irá sem incluir.
"""
print(objetos[0:2])# ['bola','borracha']

#_________________________________________________________________________________

"""
Tuplas são muito similares às listas, a diferença é que tuplas são imutáveis, e listas são mutáveis.
Ou seja, não é possível fazer a modificação de valor de um elemento na tupla. Sua reatribuição de valor
não é permitida. Para criar uma tupla você utiliza os parênteses() ao invés dos colchetes[].
"""

list_1 = ['red','blue','yellow','brown']
list_2 = list_1

print(list_1)
print(list_2)

tuple_1 = ('red','blue','yellow','brown')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

list_1[0] = 'purple'
print(list_1)
print(list_2)

# tuple[0] = 'purple' # -> TypeError
# print(tuple_1)
# print(tuple_2)

"""
Sets são os conjuntos. Eles são utilizados para identificar e 'excluir' valores que estão duplicados dentro
do nosso conjunto. Os métodos de set, são as operações matemáticas que podemos fazer com conjuntos:
Intersecção, união etc.
"""

set_1 = {'apple','watermelon','pearl','apple'}
print(set_1) 


