import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")
grupo1=data.groupby('SpanishEducation')
print(grupo1.describe())
grupo2=data.groupby('SpanishEducation').count()
print(grupo2)
grupo3=data.groupby('SpanishEducation')['YearlyIncome'].count()
print(grupo3)
grupo4=data.groupby('SpanishEducation')['YearlyIncome'].sum()
print(grupo4)
grupo5=data.groupby('Gender')['YearlyIncome'].mean()
print(grupo5)
grupo3.plot(kind='bar')
#grafico de linea vertical
plt.show()
grupo4.plot(kind='pie')
#grafica de circulo
plt.show()
grupo5.plot(kind='barh')
#grafico de linea horizontal
plt.show()
