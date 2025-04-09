# 1 Create an empty dictionary called dog
dog = {}

# 2 Add name, color, breed, legs, age to the dog dictionary
dog['color'] = 'brown'
dog['breed'] = 'vago de la calle'
dog['legs'] = True
dog['age'] = 18
print(dog)

# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = dict()
student.update({'first_name': 'papo', 'last_name': 'moralez', 'gender': 'male', 'marital_status': 'single', 'country': 'bolivia', 'city': 'gualeguaychu', 'address': 'milan 968'}) 
student['skills'] = ['navegar', 'bailar', 'cantar']
print(student) # el método update también funciona en dictionaries

# 4 Get the length of the student dictionary
print(len(student)) # 8 

# 5 Get the value of skills and check the data type, it should be a list
print(type(student['skills'])) # <class 'list'>

# 6 Modify the skills values by adding one or two skills
student['skills'].append('cocinar')
student['skills'].append('limpiar')
print(student)

# 7 Get the dictionary keys as a list
print(student.keys()) # dict_keys(['first_name', 'last_name', 'gender', 'marital_status', 'country', 'city', 'address', 'skills'])

# 8 Get the dictionary values as a list
print(student.values()) # dict_values(['papo', 'moralez', 'male', 'single', 'bolivia', 'gualeguaychu', 'milan 968', ['navegar', 'bailar', 'cantar', 'cocinar', 'limpiar']])

# 9 Change the dictionary to a list of tuples using items() method
student_lt = list(student.items()) # hay que pasarlo a lista, porque 
print('#9',student_lt) # [('first_name', 'papo'), ('last_name', 'moralez'), ('gender', 'male'), ('marital_status', 'single'), ('country', 'bolivia'), ('city', 'gualeguaychu'), ('address', 'milan 968'), ('skills', ['navegar', 'bailar', 'cantar', 'cocinar', 'limpiar'])]
print(type(student_lt))

# OBSERVACION: los métodos items(), keys() y values() no devuelven listas de por sí, sino que devuelven dict_items, dict_values o dict_keys. Estos son objetos iterable que muestran los elementos del diccionario como tuplas (clave, valor), pero no son listas. Podés iterarlo en un for, convertirlo a lista, etc., pero no podés hacer cosas como indexado (resultado[0]) directamente.

# 10 Delete one of the items in the dictionary
del student['skills']
print(student)

# 11 Delete one of the dictionaries
del student 
# print(student) # error