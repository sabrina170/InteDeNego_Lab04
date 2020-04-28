import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creamos dos funciones
datos1=np.arange(1,10)
datos2=np.arange(1,20)
#imprimimos las variables
print(datos1)
print(datos2)
#Generamos los graficos lineales
plt.plot(datos1,'o-')
plt.show()
plt.plot(datos2,'o-')
plt.show()

