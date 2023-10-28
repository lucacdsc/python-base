def decorador():
    def interna():
        pass
    return interna

@decorador
def soma(x,y):
    return x + y
 
