"""Modelo dinámico de batimiento."""
from scipy.integrate import solve_ivp

def resolver_batimiento(P,Q,R,span=(0,6.28)):
    def f(x,y):
        b,bd=y
        return [bd, R(x)-P(x)*bd-Q(x)*b]
    return solve_ivp(f, span, [0,0], method='LSODA')
