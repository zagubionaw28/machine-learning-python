# Najpierw spróbuj wykonać zadanie samodzielnie, a następnie wykorzystaj ChatGPT, lub Google Gemini lub inne narzędzie do rozwiązania tego zadania i zapisz użyte przez Ciebie prompty.Zadanie:Stwórz wykresy z irysami jako punktami na wykresie, dla dwóch zmiennych: sepal length i sepal width. Klasy irysów oznaczone są w legendzie wykresu. Zrób wykres w trzech wersjach: dane oryginalne, znormalizowane min-max i zeskalowane z-scorem.Wynik powinien przypominać ten poniżej.Co możesz powiedzieć o min, max, mean, standard deviation dla tych danych?

import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')


# Original
plt.scatter(X['sepal length (cm)'], X['sepal width (cm)'], s=35, c=y, cmap=plt.cm.brg)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Original Dataset')
legend_labels = iris.target_names
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=plt.cm.brg(i / len(legend_labels))) for i, label in enumerate(legend_labels)]
plt.legend(handles=legend_elements, loc='upper right')
plt.show()

# Min-max
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
scatter = plt.scatter(X_normalized[:, 0], X_normalized[:, 1], s=35, c=y, cmap=plt.cm.brg)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Min-Max Normalised Dataset')
legend_labels = iris.target_names
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=plt.cm.brg(i / len(legend_labels))) for i, label in enumerate(legend_labels)]
plt.legend(handles=legend_elements, loc='upper right')
plt.show()

# Z-score
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], s=35, c=y, cmap=plt.cm.brg)
legend_labels = iris.target_names
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=plt.cm.brg(i / len(legend_labels))) for i, label in enumerate(legend_labels)]
plt.legend(handles=legend_elements, loc='upper right')
plt.show()

# Obliczenie wartości statystycznych
min_values = np.min(X_scaled, axis=0)
max_values = np.max(X_scaled, axis=0)
mean_values = np.mean(X_scaled, axis=0)
std_deviation = np.std(X_scaled, axis=0)

# Wyświetlenie wyników
print("Minimalne wartości dla każdej cechy:", min_values)
print("Maksymalne wartości dla każdej cechy:", max_values)
print("Średnie wartości dla każdej cechy:", mean_values)
print("Odchylenie standardowe dla każdej cechy:", std_deviation)