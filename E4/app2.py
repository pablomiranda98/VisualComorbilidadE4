from datetime import date
from datetime import datetime
from pandas.core.frame import DataFrame
import streamlit as st
##agregamos streamlit para nuestro servidor
import pandas as pd
## agregamos pandas para cargar los datos
import seaborn as sns
#agregamos para embellecer con seaborns
import matplotlib.pyplot as plt
##importamos matplotlib
import numpy as np
#agregamos numpy

sns.set_style("whitegrid")


## se agrega titulo a la app
st.title("Cormobilidad Chile 2019")
#Texto
st.markdown("#### Te presentamos nuestro visualizador COVID-19")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto35/Comorbilidad.csv")




##se agregan dos columnas :
columna1,columna2=st.columns(2)

with columna1:
    comorbilidad = st.radio("Comorbilidad",df.Comorbilidad.unique())
    st.markdown("Su selección de comorbilidad es :"+comorbilidad)
with columna2:
    hospitalizacion = st.radio("Hospitalizacion",df.Hospitalización.unique())
    st.markdown("Paciente se encuente hospitalizado :"+hospitalizacion)




columnas=list(df.columns)


nuevo_arreglo=[]

for index in range(len(columnas)): 
    
    if index>1:
        nuevo_arreglo.append(columnas[index])


datos= df[df["Hospitalización"]==hospitalizacion]
datos2= datos[datos["Comorbilidad"]==comorbilidad]

start_time = st.slider(
    "La fecha visualizada: ",
    min_value=1, max_value=len(nuevo_arreglo), step=1)

   
filtro= pd.DataFrame(datos2.iloc[:,2:start_time+2])   
st.table(filtro)
st.write("Tiempo ubicado ", start_time)



fig,ax = plt.subplots()
to_plot=filtro
ax.plot(to_plot.T)
ax.set_title(comorbilidad)
ax.set_ylabel("Cantidad de Hospitalizados")
ax.set_xlabel("Fechas")
xs=np.arange(0,filtro.shape[1])
plt.xticks(xs,rotation=90)

st.pyplot(fig)






