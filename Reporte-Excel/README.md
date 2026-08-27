# Reporte Salarios Excel

## Introducción 
---
![Reporte Salarios Excel](Imagenes/GIF-Reporte.gif)

Este reporte esta dirigido para todas las personas que quieran buscar trabajos relacionados a datos.  
El objetivo principal de este proyecto, es mostrar los salarios, la cantidad de ofertas de trabajo y la principal plataforma para encontrar trabajo utilizada. 
## Herramientas de Exel Utilizadas 
* Formulas y funciones.
* Validación de Datos.
* Gráficos.
### Formulas y funciones
Formula para encontrar la mediana del salario anual por puesto de trabajo: 
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

Formula para encontrar la cantidad de ofertas por puesto de trabajo: 
```
=SUMPRODUCT(
  IF(
    (puestos_trabajo[job_title_short]=C15)*
    (puestos_trabajo[job_country]=filtro_pais)*
    (ISNUMBER(SEARCH(filtro_modalidad;puestos_trabajo[job_schedule_type])));
    1;
    0
  )
)
```

Formula para limpiar el texto de la modalidad de trabajo:  
```
=MID(
  C2#;
  1;
  IFS(
      ISNUMBER(SEARCH(",";C2#)); SEARCH(",";C2#)-1;
      ISNUMBER(SEARCH(" and";C2#));SEARCH(" and";C2#)-1;
      TRUE;LEN(C2#)
      )
)
```
### Validación de Datos
Validación de datos para filtrar las categorías, de puesto trabajo, país y modalidad de trabajo. 
![Validación Dato](Imagenes/GIF-Validacion-Datos.gif)
### Gráficos
