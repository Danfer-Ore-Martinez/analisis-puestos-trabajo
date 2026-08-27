# Análisis Puestos Trabajo

## Introducción 
---
Este análisis, esta enfocado, en poder detectar cuales son las habilidades con mejores sueldos y con mayor requerimiento, para poder entender que habilidades pueden dar mejor oportunidades en el mercado laboral. 

### Preguntas de Análisis 
---
Con el objetivo de entender, mejor los requerimientos laborales, se plantean 4 preguntas: 
- ¿Qué habilidades son mejor pagadas?
- ¿Cuál es la variación de los salarios según la región?
- ¿Cuales son las habilidades más requeridas?
- ¿Cuál es el salario para las 10 habilidades más requeridas?
### Herramientas de Exel Utilizadas
---
* Tablas Dinámicas 
* Gráficos Dinámicos. 
* Power Query.
* Power Pivot.
* Dax (Data Analysis Expressions). 
## 1. ¿Qué habilidades son mejor pagadas?
### Habilidad Usada: Power Query (ETL)
#### Extraer: 
Se utilizar Power Query, para poder extraer la información del archivo original `data_salary_all.xlsx`. 
#### Transformar: 
Se transforma la información original en 2 tablas diferentes. 
- data_jobs_salary: Tabla original, con algunas modificaciones, añadiendo adicional un id, para cada registro.  
![Imagen Salarios PQ](Imagenes/PQ-Salario-Trabajos.png)
- data_jobs_skills: Tabla de las habilidades requeridas, para cada solicitud.  
![Imagen Habilidades PQ](Imagenes/PQ-Habilidades-Trabajo.png)
#### Load (cargar);
Finalmente todo se carga en la hoja de calculo de Excel, para realizar tablas o gráficos.
![Cargar Datos](Imagenes/Cargar-Datos.png)

```
=ROUND(
  MEDIAN(
    IF(
      (C3=puestos_trabajo[job_title_short])*
      (filtro_pais=puestos_trabajo[job_country])*
      (ISNUMBER(SEARCH(filtro_modalidad;puestos_trabajo[job_schedule_type])))*
      (puestos_trabajo[salary_year_avg]<>0);
      puestos_trabajo[salary_year_avg]
      )
  );
  0
)
```

## Resumen 
--- 
El presente proyecto, facilita la visualización de información y permite la segmentación de información mediante la Validación de Datos. 
**CONSIDERACION**: Esta no es la mejor manera para visualizar información, lo mejor es usar POWER BI, herramienta creada para grandes volúmenes de datos, este proyecto, buscar demostrar mis capacidades en Excel, el uso de formulas, funciones, gráficos y validación de información.
## Sobre Mi 
---
Buenos días, buenas tardes o buenas noches, dependiendo de cuando leas esto, soy un Estudiante de Ing. Sistemas mi nombre es Danfer Marcelo Ore, me quiero especializar en análisis de datos, este proyecto busca demostrar mi manejo en Excel, por lo menos a un nivel básico, con formulas y gráficos, tengo proyectos con Excel requieren mayor nivel :).
