import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")
min=pd.DataFrame(data['TotalChildren']).min()
max=pd.DataFrame(data['TotalChildren']).max()
r=max-min
n=pd.DataFrame(data['TotalChildren']).count()
k=1+3.3*math.log10(n)
tic=r/k
print('min:',min,'max :',max,'cantidad:',n,'k :',k,'tic:',tic)
rango=np.arange(-0.3,5.3,0.3)

frec=pd.cut(data['TotalChildren'],rango)
tabla_frec=pd.value_counts(frec)
print(tabla_frec)

