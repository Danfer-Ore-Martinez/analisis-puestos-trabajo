from pathlib import Path
ruta = Path(__file__).parents[1] / 'Archivos'

def ruta_archivo_original()-> Path:
    return ruta / 'data_jobs.csv' 

def ruta_archivo_limpio()-> Path:
    return ruta / 'data_jobs_limpio.parquet' 
