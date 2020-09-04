# a y b hacen referencia al objeto que representa al entero 1
# Referencian a la misma dirección de memoria
a = 1
b = 1
print("primero")
id(1)
id(a)
id(b)

"""

# b es asignado con el objeto que representa el entero 2
# a y b referencian a diferentes direcciones de memoria
# a mantiene la referencia al entero 1
 b = 2
 id(a)
4299329328
 id(b)
4299329360

# a es asignada con el valor de b
# a y b referencian al mismo objeto y, por tanto,
# a la misma dirección de memoria
 a = b
 id(a)
4299329360
 a
2
"""
