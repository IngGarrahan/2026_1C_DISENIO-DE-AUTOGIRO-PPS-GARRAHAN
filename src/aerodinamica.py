"""Funciones aerodinámicas del rotor."""
import numpy as np

def fuerzas_aerodinamicas(V, Cl, Cd, A, rho=1.225):
    L = 0.5*rho*V**2*Cl*A
    D = 0.5*rho*V**2*Cd*A
    return L, D
