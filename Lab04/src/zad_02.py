# Zadanie to przypomina zadania z laboratoriów o klasyfikacji. Tym razem klasyfikatorem dla bazy danych irysów będzie
# sieć neuronowa.
# Do stworzenia i wytrenowania sieci neuronowej MLP (Multilayer perceptron) użyjemy paczki sklearn. Zadanie należy
# rozwiązywać z wykorzystaniem pomocy z internetu, polecam np. samoczuek:
# • https://python-course.eu/machine-learning/neural-networks-with-scikit.php (część “Complete Iris Dataset
# Example”). Lub:
# • https://www.kaggle.com/code/avk256/iris-with-mlpclassifier/notebook
# Co należy zrobić?
# a) Załadować paczkę sklearn , bazę danych z irysami I podzielić irysy na część testową i treningową używając
# komendy: train_test_split ( 70% / 30% ).

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neural_network import MLPClassifier # neural network
from sklearn.metrics import accuracy_score

#a)
data = pd.read_csv("iris.csv")
pd.set_option('future.no_silent_downcasting', True)
sns.pairplot( data=data, vars=('sepal.length', 'sepal.width', 'petal.length', 'petal.width'), hue='species')

#b) i c)
target = data[['species']].replace(['setosa', 'versicolor', 'virginica'],[0,1,2]).infer_objects()
df_norm = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

X = df_norm[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
Y = target['species']

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3, random_state=285763)

#d) 
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2, ), random_state=1, max_iter=3000)
#fit - funkcja trenująca
clf.fit(trainX, trainY)

#e)
# Przewidywanie etykiet dla danych testowych
predicted_labels = clf.predict(testX)
# Obliczanie dokładności
accuracy = accuracy_score(testY, predicted_labels)
print(accuracy)

#f)
clf2 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, ), random_state=1)
clf2.fit(trainX, trainY)
predicted_labels2 = clf2.predict(testX)
accuracy2 = accuracy_score(testY, predicted_labels2)
print(accuracy2)

#g)
clf3 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
clf3.fit(trainX, trainY)
predicted_labels3 = clf3.predict(testX)
accuracy3 = accuracy_score(testY, predicted_labels3)
print(accuracy3)

# Tworzenie listy z dokładnościami dla każdego klasyfikatora
accuracies = [accuracy, accuracy2, accuracy3]
classifiers = ['1 warstwa ukryta', '1 warstwa ukryta (3 neurony)', '2 warstwy ukryte (3 neurony każda)']

# Tworzenie wykresu słupkowego
plt.figure(figsize=(10, 6))
plt.bar(classifiers, accuracies, color=['blue', 'orange', 'green'])

# Dodawanie tytułu i etykiet osi
plt.title('Porównanie dokładności klasyfikatorów MLP')
plt.xlabel('Konfiguracja klasyfikatora')
plt.ylabel('Dokładność')

# Wyświetlanie wartości na słupkach
for i, v in enumerate(accuracies):
    plt.text(i, v, str(round(v, 2)), ha='center', va='bottom')

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()