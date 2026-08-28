# Análisis de Ofertas Labores para Trabajos Relacionados a Datos 

1. [Introducción](#Introducción)  
2. [Preguntas a Responder](#Preguntas-a-Responder)  
3. [Herramientas Utilizadas](#Herramientas-Utilizadas)
4. [Preparación de la información y limpieza ](#Preparación-de-la-información-y-limpieza)
5. [EDA](#EDA)
6. [Análisis](#Análisis)
7. [Sobre Mi](#Sobre-Mi)
## Introducción 
---
Ente proyecto, esta centrado en analizar las diversas ofertas laborales relacionadas al mundo de los datos, para ello se utilizan diversas herramientas para el procesamiento, limpieza, transformación y visualización de la información. 

## Preguntas a Responder 
---
1. ¿Qué habilidades son las más requeridas para los 3 puestos con más ofertas?
2. ¿Cuál es la tendencia del requerimiento de habilidades a lo largo del año?
3. ¿Cuál es el salario para las puestos con más ofertas?
4. ¿Qué habilidades son más optimas de aprender según el puesto?
5. ¿Qué categoría de habilidades son más optimas de aprender según el puesto?


## Herramientas Utilizadas 
---
Para la ejecución de este análisis, utilice diversas herramientas aprovechándome de los beneficios que estás brindan: 
- **Python:** Es la base de este análisis, es un lenguaje flexible, fácil de entender y de programar, también utilice las siguientes librerías:
    - Pandas: Utilice esta librería para transformar tipos de datos, analizar y transformar los datos.
    - Matplotlib: Permite visualizar la información mediante gráficos. 
    - Seaborn: Permite crear gráficos más avanzados y potentes.
- Jupyter Notebooks: Herramienta utilizada para ejecutar el código y que me permitió añadir anotaciones y diversos gráficos en un solo archivo.
- Visual Studio Code: Herramienta utilizada para poder ejecutar código en Python y gestionar entornos.
- GitHub: Herramienta utilizada para poder controlar las versiones y el flujo de trabajo colaborativo. 
## Preparación de la información y limpieza 
---
Etapa inicial donde cambio los tipos de datos, realizo diversas modificaciones y cargo este nuevo archivo en formato parquet: 

### Etapas ETL

#### Extracción de los datos  
Se extrae la información del archivo `data_jobs.csv`
```python
import pandas as pd 
from rutas import ruta_archivo_original, ruta_archivo_limpio
import ast

df = pd.read_csv(ruta_archivo_original())
df
```
#### Transformación de los datos
Se transforma la información para cambiar tipos de datos e información relevante: 
```python
# columna 'job_posted_date' de tipo de dato 'str' a 'date'
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# columna 'job_skills' de tipo de dato 'str' a 'list'
df['job_skills'] = df.job_skills.apply(
    lambda lista: ast.literal_eval(lista) 
    if pd.notna(lista) 
    else lista
    ) 

# columna 'job_type_skills' de tipo de dato 'str' a 'dict'
df['job_type_skills'] = df.job_type_skills.apply(
    lambda dict: ast.literal_eval(dict) 
    if pd.notna(dict) 
    else dict
    )
```
#### Carga de los datos 
Se cargan el data frame con todas las modificaciones en un nuevo archivo con formato parquet: 
```python
df.to_parquet(ruta_archivo_limpio())
```
- ¿Por qué utilizar `.parquet` y no `.csv`?
  - **Ocupa menos espacio:** Parquet utiliza compresión y un formato de almacenamiento columnar, por lo que normalmente los archivos ocupan menos espacio que los CSV.
  - **Conserva los tipos de datos:** Parquet almacena información sobre el esquema y los tipos de datos, como fechas, números, booleanos, etc. Además, puede representar estructuras más complejas, como listas o diccionarios, dependiendo de las herramientas utilizadas.
  - **Mayor eficiencia en el procesamiento:** Al ser un formato columnar, permite leer únicamente las columnas necesarias y procesar grandes volúmenes de datos de forma más eficiente que un CSV.
  - **Mantiene el esquema de los datos:** A diferencia del CSV, que básicamente almacena texto separado por delimitadores, Parquet conserva información sobre la estructura y los tipos de las columnas.

## EDA
--- 
Pequeño análisis exploratorio de los datos con la finalidad de tener un contexto general de la información que se va analizar: 
### ¿Qué Puestos de Trabajo Tiene Mayor Demanda?
![Puestos con Mayor Demanda](Imagenes/1-1-¿Que-Puestos-de-Trabajo-Tienen-Mayor-Demanda.png)
**Interpretación**: Los puestos de junior, son aquellos que tienen mayor demanda, por otro lado, los puestos de senior, tienen una demanda más baja al ser cargos que requieren mayor especialización, sin embargo, algo curioso es que los puestos de **Machine Learning Engineer** y de **Cloud Engineer** son los puestos de trabajo que tienen menos ofertas, esto puede ser, porque, ambas las suelen utilizar solo empresas grandes.

### ¿Qué Países Publican Mayor Cantidad de Ofertas de Trabajo?
![Países con Mayor Cantidad de Ofertas](Imagenes/1-2-¿Que-Paises-Publican-Mayor-Cantidad-de-Ofertas-de-Trabajo.png)
**Interpretación**: En términos generales los países más desarrollados y del primer mundo son aquellos que brindan más ofertas, liderando Estados Unidos, seguí de India que sería un caso especial, porque no es un país muy desarrollado, sin embargo, si tiene una gran cantidad de ofertas tecnológicas y fruto de ello brindan más oportunidades. 

### ¿Qué Empresas Publican Mayor Cantidad de Ofertas de Trabajo?
![Empresas con Mayor Cantidad de Ofertas](Imagenes/1-3-¿Que-Empresas-Publican-Mayor-Cantidad-de-Ofertas-de-Trabajo.png)
**Interpretación**: La empresa **Emprego**, es con diferencia la empresa que tiene mayor cantidad de ofertas de trabajo, aunque, en realidad es una plataforma similar a LinkedIn, el resto de empresas son empresas centradas en tecnologías con excepción de Walmart que es del sector retail, en términos generales como es de esperarse las empresas tecnológicas son las que más ofertas de trabajos relacionados a datos.

### ¿Cuales son los Beneficios y Requisitos laborales?
![Beneficios y Requisitos Laborales](Imagenes/1-4-Análisis-de-Beneficios-y-Requisitos-Laborales.png)
**Interpretación**: El sector tecnológico parece que todavía se mantiene firme en el trabajo presencial teniendo un 91% de las empresas teniendo trabajo presencial, por otro lado parece que el titulo tiene una importancia alta pero cada vez es menos necesaria teniendo que el 30% de las empresas no solicitan titulo para trabajar, y finalmente algo sorprendente es que el 88% de los trabajos no ofrecer seguros médicos, esto se puede deber a la modalidad de las ofertas que se publican o también a la leyes de cada país donde se publican estas ofertas. 
## Análisis 
---
### ¿Qué habilidades son las más requeridas para los 3 puestos con más ofertas?
![Habilidades Requeridas por Puestos](Imagenes/2-Porcentaje-Habilidades-Requeridas-por-Puestos.png)  
**Interpretación**: Como es de esperar, las habilidades varían según el puesto, sin embargo, existe 2 habilidades que mantienen una gran participación en los 3 puestos estas son **Python** y **SQL**, es decir, si alguien quiere ingresas al mundo de los datos, sin importan el área de especialización esta prácticamente obligado a manejar **Python** y **SQL**, luego las habilidades varían mucho según la especialización, para Data Analyst se priorizan habilidades como Excel, Power BI o Tableu, herramientas de visualización, para Data Engineer se priorizan tecnologías de nube y grandes volúmenes de datos como AWS, Azure y Spart y para Data Scientist se prioriza herramientas de análisis estadístico como R o sas.

### ¿Cuál es la tendencia del requerimiento de habilidades a lo largo del año?
![Tendencia de Habilidades a lo Largo del Año](Imagenes/3-Tendencia-de-Habilidades-Requeridas-a-lo-Largo-del-Año.png)  
**Interpretación**: La habilidades que son más estables son **SQL** y **Python**, sin embargo, tienen una pequeña caída en los meses de Agosto y Noviembre y nuevamente comienzan a tener mayor relevancia en Diciembre, el resto de habilidades tienen pequeñas variaciones a lo largo del año, pero nada con un gran impacto. 

### ¿Cuál es el salario para las puestos con más ofertas?
![Comparación Salario 5 Puestos más Ofertas](Imagenes/4-1-Comparacion-de-los-Salarios-para-los-5-Puesto-mas-Solicitados.png)  
**Interpretación**: 
![Data Analyst Mediana Habilidad mas Pagada y mas Popular](Imagenes/4-2-Data-Analyst-Mediana-Habilidad-mas-Pagada-y-mas-Popular.png)  
*Para esta ocasión me voy a centrar solo en Data Analyst*
**Interpretación**:

### ¿Qué habilidades son más optimas de aprender según el puesto?
![Habilidades mas Optimas de Aprender](Imagenes/5-Habilidadas-mas-optimas-de-aprender.png)  
**Interpretación**:

### ¿Qué categoría de habilidades son más optimas de aprender según el puesto?
![Categoría de Habilidades mas optima](Imagenes/6-Categoria-de-Habilidades-mas-Optimas-de-Aprender.png)  
**Interpretación**:

## Sobre Mi
---
