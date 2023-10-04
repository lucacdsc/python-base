# Containers são estruturas que guardam alguma coisa
# Tudo que é um container é iterável em python. Strings são iteráveis também mas não são containers.

#empacotamento
def xpto(*args):
    a = args
    print(a)   

xpto(2,3,4,5,6)

#iteração em lista
for e in [1,2,3]:
    print(e)

#listas recebem qualquer tipo de objeto
a = [1,2,3,4,5,6]
print(a)
a.append(56)
print(a)

#tuplas - gosto de lista, textura de lista mas não é uma lista.
tuple = (1,2,3,4)
print(tuple)

#conjuntos - Funcionam de fato como conjuntos. Com os métodos de união, intersecção etc.
conj = {1,2,3,4}

#dicionário - é parecido com um json
pessoa = {
    'nome':'Luca',
    'musica':'Piloto'
}