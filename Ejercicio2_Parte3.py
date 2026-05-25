# RAÍCES POR CAMBIO DE SIGNO Y BISECCIÓN 
import numpy as np
from scipy.optimize import root_scalar

# Definimos el método de bisección paso a paso
def biseccion(a, b, func, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        c = (a + b) / 2.0
        # Si llegamos al cero exacto o el margen de error es menor a la tolerancia
        if func(c) == 0 or (b - a) / 2.0 < tol: 
            return c, i+1
        # Reducimos el intervalo a la mitad
        if np.sign(func(c)) == np.sign(func(a)): 
            a = c
        else: 
            b = c
    return c, max_iter

# Definimos los intervalos viendo los cambios de signo en la tabla de V(f)
# Intervalo 1: V pasa de positivo a negativo
r1_bis, iter1 = biseccion(55.0, 57.5, cs_V)
r1_spline = root_scalar(cs_V, bracket=[55.0, 57.5], method='brentq').root

# Intervalo 2: V pasa de negativo a positivo
r2_bis, iter2 = biseccion(62.5, 65.0, cs_V)
r2_spline = root_scalar(cs_V, bracket=[62.5, 65.0], method='brentq').root

# IMPRESIÓN DE RESULTADOS
print("--- Primer Cruce por Cero (Alarma 1) ---")
print(f"Intervalo identificado: [55.0, 57.5] kHz")
print(f"Método Bisección -> Raíz: {r1_bis:.6f} kHz (en {iter1} iteraciones)")
print(f"Raíz del Spline  -> Raíz: {r1_spline:.6f} kHz")

print("\n--- Segundo Cruce por Cero (Alarma 2) ---")
print(f"Intervalo identificado: [62.5, 65.0] kHz")
print(f"Método Bisección -> Raíz: {r2_bis:.6f} kHz (en {iter2} iteraciones)")
print(f"Raíz del Spline  -> Raíz: {r2_spline:.6f} kHz")
