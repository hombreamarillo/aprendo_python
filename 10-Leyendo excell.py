
# vamos a leer unos excel con información, para sacar lo que requerimos
import xlrd as ex
import pandas as pd

# desactiva las advertecias
pd.options.mode.chained_assignment = None

ruta = "D:\HistoricoTerminales\Subsidio_201906_cierre.xlsx"
hoja = ("Base")

df2 = pd.read_excel(ruta, sheet_name = hoja)

datos = df2 [['Fecha', 'Textobrevedematerial', 'NroSerie', 'TIPOSALIDA', 'OPERACION', 'CANTIDADCOSTO', 'ABONADOCD', 'TIPOFACTURA', 'IMPORTEFINAL', 'Fecha_Venta', 'cod_abonado', 'Celular', 'Descripcion_canal', 'procedencia', 'Descripcion_Producto', 'zona', 'departamento', 'distrito', 'cod_plantarif', 'Descripcion_Segmento', 'IMPORTETOTALFINAL', 'TipoMaterial', 'Material', 'TIPOSAP', 'CANAL_LOGISTICO', 'Tipo', 'fabricante', 'ModeloTerminal']]

print(datos.head(10))
