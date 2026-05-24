import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar

# Datos originales
f = np.array([100, 120, 145, 170, 200, 235, 270, 310, 355, 405, 460, 520, 
              585, 655, 730, 810, 895, 985, 1080, 1180, 1290, 1410, 1540, 
              1680, 1830, 1990, 2160, 2340, 2530, 2730])
Z_mag = np.array([152.3, 149.1, 146.8, 144.9, 142.0, 139.5, 137.9, 136.1, 134.8, 
                  133.6, 132.7, 131.9, 131.4, 131.1, 130.9, 131.0, 131.3, 131.9, 
                  132.7, 133.8, 135.2, 136.9, 138.9, 141.1, 143.5, 146.1, 149.0, 
                  152.2, 155.6, 159.2])

# Construir Spline y su derivada
cs = CubicSpline(f, Z_mag, bc_type='natural')
cs_der1 = cs.derivative(nu=1)

# Función objetivo: g(f) = |Z|(f) - 150 = 0
Z_th = 150.0
def g(freq):
    return cs(freq) - Z_th

def g_prime(freq):
    return cs_der1(freq)

# BÚSQUEDA DE RAÍCES Y COMPARACIÓN DE MÉTODOS
# Raíz 1 (Baja frecuencia): Viendo los datos, cruza 150 entre 100Hz y 120Hz
res_bisect_1 = root_scalar(g, bracket=[100, 120], method='bisect')
res_newton_1 = root_scalar(g, x0=110, fprime=g_prime, method='newton')

# Raíz 2 (Alta frecuencia): Viendo los datos, cruza 150 entre 2160Hz y 2340Hz
res_bisect_2 = root_scalar(g, bracket=[2160, 2340], method='bisect')
res_newton_2 = root_scalar(g, x0=2200, fprime=g_prime, method='newton')

print("--- RESULTADOS DE RAÍCES ---")
print(f"Frecuencia Límite Inferior (Raíz 1): {res_newton_1.root:.4f} Hz")
print(f"Frecuencia Límite Superior (Raíz 2): {res_newton_2.root:.4f} Hz")
print("\n--- COMPARACIÓN DE MÉTODOS (Raíz 2) ---")
print(f"Bisección      -> Iteraciones: {res_bisect_2.iterations}, Convergió: {res_bisect_2.converged}")
print(f"Newton-Raphson -> Iteraciones: {res_newton_2.iterations}, Convergió: {res_newton_2.converged}")

# SENSIBILIDAD EN LA RAÍZ CERCANA A 2000 Hz
f_raiz2 = res_newton_2.root
derivada_Z = cs_der1(f_raiz2) # d|Z|/df
sensibilidad = 1 / derivada_Z # df/d|Z|

print("\n--- ANÁLISIS DE SENSIBILIDAD ---")
print(f"Derivada d|Z|/df en {f_raiz2:.2f} Hz: {derivada_Z:.5f} Ohm/Hz")
print(f"Sensibilidad (df/d|Z|): {sensibilidad:.4f} Hz/Ohm")
