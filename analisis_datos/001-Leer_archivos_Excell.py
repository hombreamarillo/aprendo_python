"""
En este código leeo unos archivos de excell para manipularlos de diferentes 
formas y sacar la informacion que estamos necesitando
"""

import xlrd as ex
import pandas as pd

# desactiva las advertecias
# pd.options.mode.chained_assignment = None


ruta = "D:Subsidio_201906_cierre.xlsx" 
hoja = ("Base")
df2 = pd.read_excel(ruta, sheet_name = hoja)

# solo selecciono las columnas que me interesan del plano, lo hago colocando el nombre de 
# cada columna ya que este archivo tiene nombre
datos = df2 [['Fecha', 'Textobrevedematerial', 'NroSerie', 'TIPOSALIDA', 'OPERACION', 'CANTIDADCOSTO', 'ABONADOCD', 'TIPOFACTURA', 'IMPORTEFINAL', 'Fecha_Venta', 'cod_abonado', 'Celular', 'Descripcion_canal', 'procedencia', 'Descripcion_Producto', 'zona', 'departamento', 'distrito', 'cod_plantarif', 'Descripcion_Segmento', 'IMPORTETOTALFINAL', 'TipoMaterial', 'Material', 'TIPOSAP', 'CANAL_LOGISTICO', 'Tipo', 'fabricante', 'ModeloTerminal']]

print(datos.head(10))

print("de nuevo la ejecute")
print("------------- Terminado -----------------------------")