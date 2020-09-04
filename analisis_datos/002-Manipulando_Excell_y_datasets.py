import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pdc_df = pd.read_csv(r"C:\Users\oscar.DESKTOP-HL4K3L2\Documents\Linux\ProgramasWinPython\data\Pdc.csv"
    , keep_default_na=False, na_values=[""],sep=';', encoding='utf-8')


ppto_df = pd.read_csv(r"C:\Users\oscar.DESKTOP-HL4K3L2\Documents\Linux\ProgramasWinPython\data\PContable.csv"
    , keep_default_na=False, na_values=[""],sep=';', encoding='utf-8')

print(pdc_df.head(0))
print("------------------------------ proceso acabado --------------------------------------")
print("Termine la tarea")

print(ppto_df.head(3))
print("------------------------------ proceso acabado --------------------------------------")
print("Termine la tarea")

pdc_sub=pdc_df.head(10)
pdc_sub_last10=pdc_df.tail(10)
pdc_sub_last10=pdc_sub_last10.reset_index(drop=True)

print("las 10 últimas")
print(pdc_sub_last10)



pila_vertical=pd.concat([pdc_sub, pdc_sub_last10], axis=0)
pila_vertical=pila_vertical.reset_index(drop=True)


pila_horizontal=pd.concat([pdc_sub, pdc_sub_last10], axis=1)

print("Fila vertical")
print(pila_vertical)

print("Fila horizontal")
print(pila_horizontal)


# Escribe el __DataFrame__ a CSV
#pila_vertical.to_csv(r"C:\Users\oscar.DESKTOP-HL4K3L2\Documents\Linux\ProgramasWinPython\data\salida_vertical.csv", index=False)
#pila_horisontal.to_csv(r"C:\Users\oscar.DESKTOP-HL4K3L2\Documents\Linux\ProgramasWinPython\data\salida_horizontal.csv", index=False)
print("---------------- describir --------------------------")
print(pila_vertical)

#print(pila_vertical['importe'])

#pila_vertical['importe'].agrupby()


              #, 'EPIGRADE_ROSETA_1' ,'Importe']


