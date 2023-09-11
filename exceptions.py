while True:
     try:
         nome = input('Digite seu nome:')
         print(nome)
         0/0
     except KeyboardInterrupt:
         print('')
         exit()
     except  ZeroDivisionError as ex:
       print('Você não pode dividir por 0')

try:
    f = open ('arquivo.txt')
except FileNotFoundError:
    print('Arquivo não existe')
else:
    print(f.read())
    f.close()
finally:
    print('Vai corinthians!')
