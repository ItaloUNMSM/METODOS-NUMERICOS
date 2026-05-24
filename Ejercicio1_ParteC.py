import numpy as np
import matplotlib.pyplot as plt
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

# Construir el Spline y obtener sus derivadas analíticas
cs = CubicSpline(f, Z_mag, bc_type='natural')
cs_der1 = cs.derivative(nu=1) # Primera derivada 
cs_der2 = cs.derivative(nu=2) # Segunda derivada 

# Búsqueda de la raíz de la primera derivada (cambio de negativa a positiva)
# Sabemos por la Parte A que el mínimo está alrededor de 730 Hz.
# Buscamos el cruce por cero entre 600 Hz y 900 Hz.
raiz = root_scalar(cs_der1, bracket=[600, 900])
f_min_exacto = raiz.root
Z_min_exacto = cs(f_min_exacto)

print(f"--- RESULTADOS DE DERIVACIÓN ---")
print(f"Frecuencia exacta del mínimo (d|Z|/df = 0): {f_min_exacto:.4f} Hz")
print(f"Magnitud |Z| en ese mínimo: {Z_min_exacto:.4f} Ohm")

# Evaluación de la segunda derivada en el mínimo
d2Z_min = cs_der2(f_min_exacto)
print(f"Segunda derivada d^2|Z|/df^2 en el mínimo: {d2Z_min:.6e} Ohm/Hz^2")

# Gráfica de la primera derivada
f_fine = np.linspace(min(f), max(f), 1000)
der1_fine = cs_der1(f_fine)
der1_nodos = cs_der1(f)

plt.figure(figsize=(10, 6))
plt.plot(f_fine, der1_fine, '-b', label='Derivada analítica del Spline $d|Z|/df$')
plt.plot(f, der1_nodos, 'ko', label='Derivada en nodos medidos')
plt.axhline(0, color='r', linestyle='--', linewidth=1.5, label='Línea de cruce por cero')
plt.plot(f_min_exacto, 0, 'go', markersize=8, label=f'Raíz exacta ({f_min_exacto:.1f} Hz)')

plt.title('Primera Derivada de la Impedancia vs Frecuencia', fontsize=14)
plt.xlabel('Frecuencia f (Hz)', fontsize=12)
plt.ylabel('$d|Z|/df$ ($\Omega$/Hz)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
