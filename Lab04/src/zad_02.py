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
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size = 0.7, random_state=285763)
