import xlrd
import pandas as pd
import numpy as np
import math
data=pd.read_excel('BI_Alumnos.xlsx',sheet_name="Hoja1")
min=pd.DataFrame(data).min()
max=pd.DataFrame(data).max()
r=max-min
n=pd.DataFrame(data).count()
k=1+3.3*math.log10(n)
tic=r/k
print(min,'',max,'',n,'',k,'',tic)
rango=np.arange(8.1,16.2,0.9)
#se suma y se resta el tic
#min=9.0, para nuestr rango 9.0-0.9=8.1
#max=15.3, para nuestr rango 15.3-0.9=16.2
frec=pd.cut(data['Nota'],rango)
tabla_frec=pd.value_counts(frec)
print(tabla_frec)