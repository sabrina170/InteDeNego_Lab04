import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv('Ventas.csv')
ventas=pd.DataFrame(data)
print(ventas)
mes=ventas['Meses']
mon=ventas['Monto']

plt.plot(mes,mon,'o-')
plt.title("Ventas Enero-Junio")
plt.ylabel("Monto")
plt.xlabel("Meses")
plt.show()
