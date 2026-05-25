import numpy as np
from scipy.interpolate import lagrange, CubicSpline

# DATOS DEL ENSAYO
f = np.array([10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 
              45.0, 47.5, 50.0, 52.5, 55.0, 57.5, 60.0, 62.5, 65.0, 67.5, 70.0, 72.5, 75.0, 
              77.5, 80.0, 82.5, 85.0, 87.5, 90.0, 92.5, 95.0, 97.5, 100.0, 102.5, 105.0, 107.5])

V = np.array([0.842, 0.911, 0.986, 1.062, 1.143, 1.227, 1.314, 1.401, 1.482, 1.551, 1.216, 1.048, 0.866, 0.689,
              0.521, 0.364, 0.223, 0.103, 0.012, -0.041, -0.057, -0.034, 0.018, 0.096, 0.197, 0.318, 0.452,
              0.579, 0.700, 0.809, 0.611, 0.688, 0.756, 0.811, 0.856, 0.894, 0.926, 0.954, 0.980, 1.004])

Z = np.array([182.4, 178.9, 175.1, 171.0, 166.8, 162.7, 158.9, 155.4, 152.0, 149.0, 146.1, 145.2, 145.8, 147.3,
              149.9, 153.5, 158.0, 163.2, 168.9, 174.8, 180.5, 186.2, 191.5, 196.2, 200.1, 203.1, 205.2,
              206.3, 206.1, 204.7, 198.0, 194.4, 190.9, 187.8, 185.1, 183.0, 181.6, 180.8, 180.6, 180.9])

# Interpolación Lagrange (3 puntos más cercanos)
# Para f=41.0 kHz usamos los índices correspondientes a 37.5, 40.0 y 42.5
f_41 = f[11:14]; V_41 = V[11:14]; Z_41 = Z[11:14]
lag_V_41 = lagrange(f_41, V_41)(41.0)
lag_Z_41 = lagrange(f_41, Z_41)(41.0)

# Para f=73.0 kHz usamos los índices correspondientes a 70.0, 72.5 y 75.0
f_73 = f[24:27]; V_73 = V[24:27]; Z_73 = Z[24:27]
lag_V_73 = lagrange(f_73, V_73)(73.0)
lag_Z_73 = lagrange(f_73, Z_73)(73.0)

# Spline Cúbico Natural
cs_V = CubicSpline(f, V, bc_type='natural')
cs_Z = CubicSpline(f, Z, bc_type='natural')

# IMPRESIÓN DE RESULTADOS 
print("--- Resultados f = 41.0 kHz ---")
print(f"Lagrange -> V: {lag_V_41:.4f} V  |  |Z|: {lag_Z_41:.4f} Ohm")
print(f"Spline   -> V: {cs_V(41.0):.4f} V  |  |Z|: {cs_Z(41.0):.4f} Ohm")

print("\n--- Resultados f = 73.0 kHz ---")
print(f"Lagrange -> V: {lag_V_73:.4f} V  |  |Z|: {lag_Z_73:.4f} Ohm")
print(f"Spline   -> V: {cs_V(73.0):.4f} V  |  |Z|: {cs_Z(73.0):.4f} Ohm")
