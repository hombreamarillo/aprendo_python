# Repaso de el tema de Funciones
"""
este block de trabajo es para aprender todo sobre lso metodos
en python ya que estory aprendiedo a usar este en programación orientada a
objetos
"""

print("Comensamos con el uso de Funciones")

divisas = {"PEN": 3.256, "MXN": 20, "PESO": 3745.41}


def definir_tipo_cambio(tipo_moneda, valor_cambio):
    divisas[tipo_moneda] = valor_cambio
    return


def convertir(monto_inicial, tipo_moneda="PESO"):
    valor = divisas.get(tipo_moneda)
    monto_final = monto_inicial * valor
    return monto_final


print("Ingrese la moneada y el valor del cambio separados por (,)")
texto = str(input()).split(",")
moneda = texto[0]
valor_cambio = float(texto[1])

definir_tipo_cambio(moneda, valor_cambio)
print("Ingrese el monto de Dinero a convertir de " + moneda + " a USD")
monto = float(input())
resultado = convertir(monto, moneda)
print(str(monto) + " " + str(moneda) + "  en USD es  " + str(resultado))
