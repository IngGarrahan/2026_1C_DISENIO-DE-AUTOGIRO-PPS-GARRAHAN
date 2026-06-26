"""Carga de coeficientes aerodinámicos obtenidos de XFoil."""
import pandas as pd

def cargar_archivo(path):
    return pd.read_csv(path)
