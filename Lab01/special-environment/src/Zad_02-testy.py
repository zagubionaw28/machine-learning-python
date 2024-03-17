import numpy as np
import matplotlib.pyplot as plt

# Funkcja opisująca trajektorię
def trajectory(x):
    return -0.01 * x**2 + 100

# Generowanie punktów x od 0 do 200
x_values = np.linspace(0, 200, 400)
# Obliczenie odpowiadających im wartości y
y_values = trajectory(x_values)

# Rysowanie wykresu
plt.plot(x_values, y_values, color='blue', linewidth=2)
plt.xlabel('Odległość')
plt.ylabel('Wysokość')
plt.title('Trajektoria lotu')
plt.grid(True)
plt.show()
