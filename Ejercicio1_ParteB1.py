import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import random

# Datos
f = np.array([100, 120, 145, 170, 200, 235, 270, 310, 355, 405, 460, 520, 
              585, 655, 730, 810, 895, 985, 1080, 1180, 1290, 1410, 1540, 
              1680, 1830, 1990, 2160, 2340, 2530, 2730])
Z_mag = np.array([152.3, 149.1, 146.8, 144.9, 142.0, 139.5, 137.9, 136.1, 134.8, 
                  133.6, 132.7, 131.9, 131.4, 131.1, 130.9, 131.0, 131.3, 131.9, 
                  132.7, 133.8, 135.2, 136.9, 138.9, 141.1, 143.5, 146.1, 149.0, 
                  152.2, 155.6, 159.2])

# Método Matricial (Vandermonde)
# Intentamos calcular el grado 29 directamente (generará advertencias por mal condicionamiento)
V = np.vander(f, N=len(f), increasing=True)
try:
    coef_matricial = np.linalg.solve(V, Z_mag)
except np.linalg.LinAlgError as e:
    print(f"Error en Método Matricial: {e} (Matriz singular/Mal condicionada)")

# Método de Lagrange
poly_lagrange = lagrange(f, Z_mag)

# Polinomios Escalonados (Grados 5, 10, 15 y 29) 
# Usamos polyfit para ajustar (mínimos cuadrados para grados menores, interpolación para grado 29)
import warnings
warnings.simplefilter('ignore') # Forma general de ocultar el warning del grado 29

p_5 = np.poly1d(np.polyfit(f, Z_mag, 5))
p_10 = np.poly1d(np.polyfit(f, Z_mag, 10))
p_15 = np.poly1d(np.polyfit(f, Z_mag, 15))
p_29 = np.poly1d(np.polyfit(f, Z_mag, 29))

# Gráfico para evidenciar el Fenómeno de Runge
f_fine = np.linspace(min(f), max(f), 1000)
plt.figure(figsize=(12, 7))
plt.plot(f, Z_mag, 'ko', label='Datos reales', zorder=5)
plt.plot(f_fine, p_5(f_fine), label='Grado 5', linewidth=2)
plt.plot(f_fine, p_10(f_fine), label='Grado 10', linewidth=1.5)
plt.plot(f_fine, p_15(f_fine), label='Grado 15', linewidth=1)
plt.plot(f_fine, p_29(f_fine), '--r', label='Grado 29 (Oscilaciones severas)', linewidth=1)
plt.ylim(120, 170) # Limitamos el eje Y porque los grados altos explotan
plt.title('Comparación de Polinomios: Evidencia del Fenómeno de Runge')
plt.xlabel('Frecuencia f (Hz)')
plt.ylabel('Impedancia |Z| (Ohm)')
plt.legend()
plt.grid(True)
plt.show()

# Cálculo en f = 1000 Hz con Polinomio Seleccionado (Grado 5)
f_target = 1000
Z_1000_poly = p_5(f_target)
print(f"\nValor interpolado en f=1000 Hz (Grado 5): {Z_1000_poly:.2f} Ohm")

# Validación Leave-One-Out (LOO) con 5 puntos al azar
random.seed(42) # Para reproducibilidad
indices_azar = random.sample(range(len(f)), 5)
errores_relativos = []

print("\n--- Validación LOO (Grado 5) ---")
for idx in indices_azar:
    # Separar datos de entrenamiento y el punto de prueba
    f_train = np.delete(f, idx)
    Z_train = np.delete(Z_mag, idx)
    f_test = f[idx]
    Z_test_real = Z_mag[idx]
    
    # Entrenar modelo sin ese punto
    p_train = np.poly1d(np.polyfit(f_train, Z_train, 5))
    Z_pred = p_train(f_test)
    
    # Calcular error relativo
    err_rel = abs((Z_pred - Z_test_real) / Z_test_real) * 100
    errores_relativos.append(err_rel)
    print(f"Punto omitido: {f_test} Hz | Real: {Z_test_real} | Predicho: {Z_pred:.2f} | Error: {err_rel:.2f}%")

print(f"Error relativo promedio estimado (LOO): {np.mean(errores_relativos):.2f}%")
