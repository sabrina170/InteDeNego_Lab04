import xlrd
import pandas as pd
import numpy as np
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")
rango=np.arange(-1,6,1)
#creamos un arreglo que identifica el valor minimo y manximo
frecuencia=pd.cut(data['TotalChildren'],rango)
#identifico un varibles
tabla=pd.value_counts(frecuencia)
#armando nuestra frecuencia
print(tabla)