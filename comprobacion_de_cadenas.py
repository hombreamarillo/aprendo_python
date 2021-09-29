
def is_empty(data_structure):
    if data_structure:
        print("No está vacía")
        return False
    else:
        print("Está vacía")
        return True


d = {}
t = ()
l = []
str = ''
s = set()


is_empty(d)
is_empty(t)
is_empty(l)
is_empty(s)


print('Vamos a añadir un elemento a cada estructura')


d['a'] = 1
t = tuple('a')
l.append('a')
str = 'a'
s.add('a')


is_empty(d)
print(d)
is_empty(t)
print(t)
is_empty(l)
print(l)
is_empty(s)
print(s)


nombre='Oscar Alfonso'
apellidos = 'López Aguilar'
nombre_completo = nombre + ' ' + apellidos
print(nombre_completo)
print('esto es un saludo para %s que se apellida %s' % (nombre,apellidos))



#la forma más eficiente d eforatear strings
animal ='perro'
comida = 'carne'
print( f'el {animal} come demasiada {comida} , todos los días')

print('\n')
