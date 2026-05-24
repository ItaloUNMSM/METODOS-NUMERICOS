import numpy as np
import matplotlib.pyplot as plt

# Definición de los datos del experimento, frecuencias en Hz

f = np.array([100, 120, 145, 170, 200, 235, 270, 310, 355, 405, 460, 520, 
              585, 655, 730, 810, 895, 985, 1080, 1180, 1290, 1410, 1540, 
              1680, 1830, 1990, 2160, 2340, 2530, 2730])

# Magnitud de impedancia en Ohm
Z_mag = np.array([152.3, 149.1, 146.8, 144.9, 142.0, 139.5, 137.9, 136.1, 134.8, 
                  133.6, 132.7, 131.9, 131.4, 131.1, 130.9, 131.0, 131.3, 131.9, 
                  132.7, 133.8, 135.2, 136.9, 138.9, 141.1, 143.5, 146.1, 149.0, 
                  152.2, 155.6, 159.2])

# Identificación computacional del mínimo local
indice_minimo = np.argmin(Z_mag)
f_min = f[indice_minimo]
Z_min = Z_mag[indice_minimo]

print(f"Mínimo local encontrado en: f = {f_min} Hz, |Z| = {Z_min} Ohm")

# Generación del Gráfico
plt.figure(figsize=(10, 6))
plt.plot(f, Z_mag, marker='o', linestyle='-', color='b', linewidth=1.5, markersize=5, label='Datos medidos $|Z|(f)$')

# Resaltar el punto mínimo en el gráfico
plt.plot(f_min, Z_min, marker='o', color='r', markersize=8, 
         label=f'Mínimo local aprox. ({f_min} Hz, {Z_min} $\Omega$)')

# Configuración del gráfico
plt.title('Magnitud de Impedancia Bioeléctrica vs Frecuencia', fontsize=14)
plt.xlabel('Frecuencia f (Hz)', fontsize=12)
plt.ylabel('Magnitud de Impedancia $|Z|$ ($\Omega$)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=11)
plt.tight_layout()

# Mostrar grafico
plt.show()
