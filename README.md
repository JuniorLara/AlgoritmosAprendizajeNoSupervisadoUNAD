# Algoritmos de Aprendizaje no Supervisado - Actividad 4
![Logo UNAD](https://datateca.unad.edu.co/contenidos/publicaciones/Comunicaciones_VIMEP/course-images/GENERAL/es/logoUNAD-HD.webp)

## Descripción
Este proyecto tiene como objetivo aplicar y evaluar dos algoritmos de clustering: **K-means** y **Hierarchical Clustering**, con el fin de agrupar un conjunto de datos basado en las similitudes entre sus características. El proceso incluye un análisis exploratorio de datos, preprocesamiento, selección de características, entrenamiento de modelos y evaluación utilizando diversas métricas. Además, se realizarán visualizaciones que ayudarán a interpretar los resultados obtenidos.

## Estructura del Proyecto
El proyecto se organiza en 2 carpetas principales, cada una destinada a un aspecto clave del análisis:

- **Datasets**: Almacena los archivos CSV necesarios para los diferentes ejercicios y análisis a realizar.
- **Business**: Contiene la lógica de negocio y el enfoque utilizado para el análisis exploratorio.

En este proyecto, se realiza un análisis exploratorio profundo y se implementan diversas técnicas de predicción, tales como:
- **K-Means**: Es un algoritmo de clustering basado en particionar los datos en un número predefinido de grupos (K). Su objetivo es minimizar la varianza dentro de cada cluster, asegurando que los puntos dentro de un mismo cluster sean lo más similares posible. 
- **Hierarchical Clustering**:  crea una jerarquía de clusters, donde cada punto de datos comienza como un cluster independiente y se fusiona progresivamente con otros clusters más cercanos (en el caso del enfoque aglomerativo) o un único cluster se divide en subgrupos (en el enfoque divisivo).

Los archivos Jupyter Notebook incluidos en el proyecto y sus objetivos son:

- **customer_k_means.ipynb**: Este archivo se enfoca en la implementación y evaluación del algoritmo K-means.
- **customer_hierarchical_clustering.ipynb**: Este archivo se enfoca en la implementación y evaluación del algoritmo Hierarchical Clustering.

## Instalación
Para poder ejecutar este proyecto, asegúrate de tener instalados los siguientes elementos:

- [Anaconda](https://www.anaconda.com/products/distribution): Una plataforma de distribución de Python que facilita la gestión de paquetes y entornos.
- [Jupyter Notebook](https://jupyter.org/install): Una aplicación web que permite crear y compartir documentos que contienen código, ecuaciones y visualizaciones.

## Uso
1. Clona este repositorio o descarga los archivos directamente desde la fuente.
2. Abre **Anaconda Navigator** y lanza **Jupyter Notebook** desde la interfaz.
3. Navega hasta la carpeta del proyecto y abre los archivos correspondientes (`customers.ipynb`).
4. Ejecuta las celdas en cada notebook para seguir el proceso de análisis y visualización de los datos.

