#Dicionários em python ou hashmaps são pares de chave e valor. Parecido com os objetos em JavaScript.

student = {'name': 'Luca', 'age': 22, 'favoriteFood': 'Pizza', 'favoriteSong': 'Interlude-EDEN'}
print(student)
print(student.get('name'))

for key,value in student.items():
    print(key,value)