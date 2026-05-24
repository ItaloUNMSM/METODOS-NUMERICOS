from scipy.interpolate import CubicSpline

# Construcción del Spline Cúbico Natural
# bc_type='natural' impone que la segunda derivada sea cero en los extremos
cs = CubicSpline(f, Z_mag, bc_type='natural')

# Evaluación en malla fina y comparación
Z_spline_fine = cs(f_fine)

plt.figure(figsize=(10, 6))
plt.plot(f, Z_mag, 'ko', label='Datos medidos')
plt.plot(f_fine, p_5(f_fine), '--g', label='Polinomio Grado 5', alpha=0.7)
plt.plot(f_fine, Z_spline_fine, '-b', label='Spline Cúbico Natural', linewidth=2)
plt.title('Comparación: Spline Cúbico Natural vs Polinomio')
plt.xlabel('Frecuencia f (Hz)')
plt.ylabel('Impedancia |Z| (Ohm)')
plt.legend()
plt.grid(True)
plt.show()

# Cálculo en f = 1000 Hz
Z_1000_spline = cs(1000)
print(f"Valor interpolado en f=1000 Hz (Spline): {Z_1000_spline:.2f} Ohm")
