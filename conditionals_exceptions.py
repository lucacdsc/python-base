"""
Condicionais são verificações que fazemos para checar se determinada condição é verdadeira ou falsa.
E de acordo de como ela for avaliada definimos como nosso código se comportará.
"""

#Example 1.

# name1 = 'xpto'

# if name1 == 'xyz':
#     print('The name is ' + name1)
# else:
#     print('The name isn\'t xpto')


# #Example 2.
# name2 = 'kzk'

# if name2 == 'xpto':
#     print('abc')
# elif name2 == 'kzk':
#     print('def')
# else:
#     print('no match')


#Exceptions
"""
Uma exceção ocorre quando um algo inesperado ocorre ou existe um erro na execução do nosso programa.
Podemos criar exceções para tratar esses erros de maneira mais estruturada e garantir robustez ao nossos programas.
"""
try:
    a = 1
    "Hello" + "" + "Sir"
    1/0
except ZeroDivisionError as err:
    print(err)
#Runs if exception occurs in try block
else:
    print(a)
#Executes if try block *succeeds*

finally:
    print('This always executes')
#This code *always* executes



#Example 3.

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('You can\'t divide by zero')
except ValueError as e:
    print(e)
    print('You can\'t divide by a str')
except Exception:
    print('Something went wrong :(')
else:
    print(result)
finally:
    print('This always execute')