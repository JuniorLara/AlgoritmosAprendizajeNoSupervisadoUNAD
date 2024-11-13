# Importo mi Clase con las constantes declaradas con las rutas y algunos mensajes que utilizare
from Business.constants import MagicString

# Librerias para analisis Exploratorio
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px

# Librerias para implementar modelo KMeans
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Librerias para evaluar modelo
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

import warnings
warnings.filterwarnings('ignore')

class General:
    def leer_datos_csv(ruta : str):
        Datos = pd.read_csv(ruta)

        # Remuevo registros que puedan estar duplicados
        Datos.drop_duplicates(inplace=True)

        return Datos
    

    def realizar_lectura_datos_analisis(datos : pd.DataFrame, cantidad_registros : int):
        return datos.head(cantidad_registros)


    def describir_datos_csv(datos: pd.DataFrame):
        return datos.describe()


    def modificar_columna_genero(Datos: pd.DataFrame, columna : str):
        Datos[columna] = Datos[columna].replace('Male', 1)
        Datos[columna] = Datos[columna].replace('Female', 2)

        return Datos[columna]


    def realizar_imputacion_de_datos_para_datos_atipicos(datos : pd.DataFrame, nombre_columna: str) -> pd.DataFrame:
        # Calculo el Quartile 1 y Quartile 3
        Q1 = datos[nombre_columna].quantile(0.25)
        Q3 = datos[nombre_columna].quantile(0.75)
        IQR = Q3 - Q1

        #defino los limites de mis datos.
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        # Calcular la mediana
        mediana = datos[nombre_columna].median()

        # Imputar outliers con la mediana
        return  datos[nombre_columna].mask((datos[nombre_columna] < limite_inferior) | (datos[nombre_columna] > limite_superior), mediana)


    def graficar_datos_atipicos(Datos: pd.DataFrame, columna : str):
        plt.figure(figsize=(6,3))
        sns.boxplot(x=Datos[columna])
        plt.title(MagicString.TITLE_VALORES_ATIPICOS.format(columna),fontsize=10)

    
    def graficar_datos_dispersion(Datos: pd.DataFrame, columna_x: str, columna_y: str, title: str):
        plt.scatter(Datos[columna_x], Datos[columna_y])
        plt.xlabel(columna_x)
        plt.ylabel(columna_y)
        plt.title(title)
        plt.show

    def grafica_dispersion_agrupada(Datos: pd.DataFrame, columna_x: str, columna_y: str, columna_grupo: str, title: str):
        plt.scatter(Datos[columna_x], Datos[columna_y], c=Datos[columna_grupo], cmap='viridis')
        plt.xlabel(columna_x)
        plt.ylabel(columna_y)
        plt.title(title)
        plt.show

    def grafica_de_codo(numero_clusters, score):
        plt.plot(numero_clusters, score, marker=MagicString.GRAFICA_CODO_MARKER)
        plt.xlabel(MagicString.TITLE_NUMERO_CLUSTER)
        plt.ylabel(MagicString.TITLE_SCORE)
        plt.title(MagicString.TITLE_GRAFICA_DE_CODO)
        plt.show

    def generar_clusters_y_score_kmeans(Datos: pd.DataFrame, rango_valor_minimo: int, rango_valor_maximo: int):
        numero_clusters = range(rango_valor_minimo, rango_valor_maximo)

        kmeans = [KMeans(n_clusters=i) for i in numero_clusters]
        score = [kmeans[i].fit(Datos).score(Datos) for i in range(len(kmeans))]

        return (numero_clusters, kmeans, score)
    
    
    def generar_modelo_agrupamiento_kmeans(numero_agrupamientos: int, Datos: pd.DataFrame):
        Modelo = KMeans(n_clusters=10, random_state=0)
        Modelo.fit(Datos)

        return Modelo
    
    def evaluar_desempeño_modelo(Modelo, Datos: pd.DataFrame, columna: str, title_modelo: str):
        cantidad_elementos = len(Datos)
        X = Datos.drop(columna, axis=1)
        cluster = Datos[columna]

        # Calcular metricas
        sil_score = silhouette_score(X, cluster)
        calinski_score = calinski_harabasz_score(X, cluster)
        davies_score = davies_bouldin_score(X, cluster)

        # Mostrar Resultados de las metricas.
        print("=============================================================")
        print(title_modelo)
        print("=============================================================")
        print("Cantidad Elementos Evaluados:  {}".format(cantidad_elementos))
        print("Coeficiente Silhouette:        {}".format(sil_score))
        print("Indice Calinski Harabasz:      {}".format(calinski_score))
        print("Indice Davies Bouldin:         {}".format(davies_score))
