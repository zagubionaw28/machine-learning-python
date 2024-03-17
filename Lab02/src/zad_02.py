# Ściągnij czystą, bezbłędną bazę danych z irysami:•ze strony przedmiotu•lub z Internetu (Google: iris dataset csv)•lub pobierając z paczki sklearn datasets. Następnie wykorzystując technikę PCA, chcemy skompresować bazę danych z czterech do trzech lub dwóch kolumn numerycznych, nie tracąc przy tym zbyt wiele informacji.

# Wybierz paczkę i samouczek do zadania, np.:•https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html•https://notebook.community/hershaw/data-science-101/course/class1/pca/iris/PCA%20-%20Iris%20dataset•https://builtin.com/machine-learning/pca-in-pythonMożesz też skorzystać z programu pokazanego na wykładzie:

# Dokonaj PCA na bazie danych. Przyjrzyj się nowym kolumnom i wariancjom. Ile kolumn można usunąć, tak aby zachować minimum 95% wariancji (strata informacji nie może być większa niż 5%)? Korzystając z poniższego wzoru, swoją odpowiedź uzasadnij.

# 𝑆𝑡𝑟𝑎𝑡𝑎 𝑖𝑛𝑓𝑜𝑟𝑚𝑎𝑐𝑗𝑖 𝑠𝑝𝑜𝑤𝑜𝑑𝑜𝑤𝑎𝑛𝑎 𝑢𝑠𝑢𝑛𝑖ę𝑐𝑖𝑒𝑚 𝑖 𝑜𝑠𝑡𝑎𝑡𝑛𝑖𝑐ℎ 𝑘𝑜𝑙𝑢𝑚𝑛 = ∑𝑉𝑎𝑟(𝑘𝑜𝑙𝑢𝑚𝑛𝑎[𝑘])𝑛−1𝑘=𝑛−𝑖∑𝑉𝑎𝑟(𝑘𝑜𝑙𝑢𝑚𝑛𝑎[𝑘])𝑛−1𝑘=0Bazę danych z usuniętymi kolumnami zobrazuj na wykresie punktowym, gdzie każdy punkt to irys. Jeśli w bazie zostawisz 2 kolumny, to wykres będzie na płaszczyźnie, a jeśli 3, to będzie trójwymiarowy. Przykłady:

# entropia = porozrzucane dane

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')
print(X.head())

pca_iris = PCA(n_components=2).fit_transform(iris.data)
# print(pca_iris)
# print(pca_iris.explained_variance_ratio_.sum(), "współczynnik wariancji")
# print(pca_iris.components_, "komponenty")
# print(pca_iris.transform(iris.data), "dane irysów")

# Mogę usunąć dwie kolumny, tak aby zachować minimum 95% wariancji, ponieważ suma współczynników wariancji dwóch kolumn wynosi ponad 97%.

# plt.figure(2, figsize=(8, 6))
# plt.clf()

# Plot the training points
plt.scatter(pca_iris[:, 0], pca_iris[:, 1], s=35, c=y, cmap=plt.cm.brg)
plt.xlabel("P.C. 1")
plt.ylabel("P.C. 2")
# Tworzenie legendy dla klas
legend_labels = iris.target_names
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=plt.cm.brg(i / len(legend_labels))) for i, label in enumerate(legend_labels)]
plt.legend(handles=legend_elements, loc='lower right')
plt.show()

# Dodanie legendy do wykresu
