# Containers são estruturas que guardam alguma coisa
# Tudo que é um container é iterável em python. Strings são iteráveis também mas não são containers.

#empacotamento
def xpto(*args):
    a = args
    print(a)   

xpto(2,3,4,5,6)

#iter
for e in [1,2,3]:
    print(e)

#listas recebem qualquer tipo de objeto
a = [1,2,3,4,5,6]
print(a)
a.append(56)
print(a)