# DERIVACIÓN NUMÉRICA dV/df
import numpy as np

# El paso de frecuencia en nuestros datos es constante: 2.5 kHz
h = 2.5 

# Fórmulas matemáticas de diferencias finitas
def df_central_O2(idx): 
    return (V[idx+1] - V[idx-1]) / (2*h)
    
def df_central_O4(idx): 
    return (-V[idx+2] + 8*V[idx+1] - 8*V[idx-1] + V[idx-2]) / (12*h)
    
def df_progresiva_O2(idx): 
    return (-3*V[idx] + 4*V[idx+1] - V[idx+2]) / (2*h)

# Obtenemos la derivada exacta del Spline Cúbico
cs_V_der = cs_V.derivative(1)

# Buscamos las posiciones (índices) exactas en la tabla
i_40 = np.where(f == 40.0)[0][0]
i_70 = np.where(f == 70.0)[0][0]
i_100 = np.where(f == 100.0)[0][0]
i_10 = np.where(f == 10.0)[0][0]

# IMPRESIÓN DE RESULTADOS
print("--- Resultados de Sensibilidad (dV/df) ---")

for freq, idx in zip([40.0, 70.0, 100.0], [i_40, i_70, i_100]):
    print(f"\n--- En f = {freq} kHz ---")
    print(f"Dif. Centrada (Orden 2): {df_central_O2(idx):.6f} V/kHz")
    print(f"Dif. Centrada (Orden 4): {df_central_O4(idx):.6f} V/kHz")
    print(f"Derivada del Spline:     {cs_V_der(freq):.6f} V/kHz")

print(f"\n--- En f = 10.0 kHz (Extremo inicial) ---")
print(f"Dif. Progresiva (Orden 2): {df_progresiva_O2(i_10):.6f} V/kHz")
print(f"Derivada del Spline:       {cs_V_der(10.0):.6f} V/kHz")
