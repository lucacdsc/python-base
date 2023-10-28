#Closure é uma função que possui outra função aninhada dentro dela.


def externa():
    def interna():
        print(42)
    return interna

func = externa()
func()

def criar_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contador1 = criar_contador()
contador2 = criar_contador()

print(contador1())
print(contador2())