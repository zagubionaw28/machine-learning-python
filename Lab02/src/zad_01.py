# BŁĘDY I BRAKUJĄCE DANE W IRYSACH
# Ściągnij ze strony zajęć plik iris_with_errors.csv. Znajduje się w nim baza danych z irysami, jednak są w niej błędy.
# Celem zadania jest poprawienie tych błędów. Zamiast jednak ręcznego szukania i poprawiania, wykorzystajmy do tego
# specjalistyczne paczki. W języku Python można to zrobić z wykorzystaniem paczki Pandas:import 
# • https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-
# 3e9c6ebcf78b
# • https://realpython.com/python-data-cleaning-numpy-pandas/
# Wykorzystując powyższe linki i technologie w nich zaprezentowane napraw bazę iris_with_errors.csv. Postaraj się
# wykonać następujące kroki.
# a) Policz ile jest w bazie brakujących lub nieuzupełnionych danych. Wyświetl statystyki bazy danych z błędami.
# b) Sprawdź czy wszystkie dane numeryczne są z zakresu (0; 15). Dane spoza zakresu muszą być poprawione. Możesz
# tutaj użyć metody: za błędne dane podstaw średnią (lub medianę) z danej kolumny.
# c) Sprawdź czy wszystkie gatunki są napisami: „Setosa”, „Versicolor” lub „Virginica”. Jeśli nie, wskaż jakie popełniono
# błędy i popraw je własną (sensowną) metodą.

import pandas as pd
import numpy as np
import math

# a) Policz ile jest w bazie brakujących lub nieuzupełnionych danych. Wyświetl statystyki bazy danych z błędami.

# Wczytaj plik CSV, wskazując że kolumny są oddzielone przecinkami
df = pd.read_csv('iris_with_errors.csv', delimiter=',')

# Making a list of missing value types
missing_values = ["NA", "-"]
df = pd.read_csv("iris_with_errors.csv", na_values = missing_values)

# Zlicz brakujące lub nieuzupełnione dane w każdej kolumnie
brakujace_dane = df.isnull().sum()

# Wyświetl wyniki
print(brakujace_dane)

# b) Sprawdź czy wszystkie dane numeryczne są z zakresu (0; 15). Dane spoza zakresu muszą być poprawione. Możesz
# tutaj użyć metody: za błędne dane podstaw średnią (lub medianę) z danej kolumny.

def count_average(name, array):
  average = 0
  counter = 0
  for i in array.values:
    if isinstance(i, (int, float)) and not math.isnan(i) and i > 0 and i < 15:
      average += i
      counter += 1
  if counter != 0:
    average = average/counter
  print(name, average)

  return average

def changeForAverage(average, array):
  for idx, i in enumerate(array.values):
    if not isinstance(i, (int, float)) or math.isnan(i) or i < 0 or i > 15 or i == 0.0:
      print(i)
      array.values[idx] = averageA
      print(array.values[idx], "zmiana")
  is_in_range = (array.values > 0) & (array.values < 15)
  if (is_in_range.all() == False):
      ilosc_false = len(is_in_range) - sum(is_in_range)
      print("Liczba wartości False w tablicy is_in_range_A:", ilosc_false)
      # Dodaj drugie wywołanie print, aby wyświetlić wartości, które nadal są False
      print("Wartości spoza zakresu:")
      for value in array.values:
          if value <= 0 or value >= 15:
              print(value)


is_in_range_A = (df['sepal.length'] > 0) & (df['sepal.length'] < 15)
if (is_in_range_A.all() == False):
  averageA = count_average("sepal.length", df['sepal.length'])
  changeForAverage(averageA, df['sepal.length'])

  
print("---------------------------------------------------B")
is_in_range_B = (df['sepal.width'] > 0) & (df['sepal.width'] < 15)
if (is_in_range_B.all() == False):
  averageB = count_average("sepal.width", df['sepal.width'])
  changeForAverage(averageB, df['sepal.width'])

print("---------------------------------------------------C")
is_in_range_C = (df['petal.length'] > 0) & (df['petal.length'] < 15)
if (is_in_range_C.all() == False):
  averageC = count_average('petal.length', df['petal.length'])
  changeForAverage(averageC, df['petal.length'])

print("---------------------------------------------------D")
is_in_range_D = (df['petal.width'] > 0) & (df['petal.width'] < 15)
if (is_in_range_D.all() == False):
  averageD = count_average('petal.width', df['petal.width'])
  changeForAverage(averageD, df['petal.width'])

# c) Sprawdź czy wszystkie gatunki są napisami: „Setosa”, „Versicolor” lub „Virginica”. Jeśli nie, wskaż jakie popełniono
# błędy i popraw je własną (sensowną) metodą.

is_in_range_E = (df["variety"] == "Setosa") | (df["variety"] == "Versicolor") | (df["variety"] == "Virginica")
if (is_in_range_E.all() == False):
    ilosc_false = len(is_in_range_E) - sum(is_in_range_E)
    print("Liczba wartości False w tablicy is_in_range_A:", ilosc_false)
    for idx, value in enumerate(df["variety"].values):
          if value != "Setosa" and value != "Versicolor" and value != "Virginica":
              if value == 'setosa' or value == 'versicolor' or value == 'virginica':
                print(value)
                firstLetter = value[0].capitalize()
                df["variety"].values[idx] = firstLetter + value[1:]
                print(df["variety"].values[idx], "zmiana")
              if value == 'Versicolour':
                df["variety"].values[idx] = 'Versicolor'
is_in_range_E = (df["variety"] == "Setosa") | (df["variety"] == "Versicolor") | (df["variety"] == "Virginica")
if (is_in_range_E.all() == False):
  ilosc_false = len(is_in_range_E) - sum(is_in_range_E)
  print("Liczba wartości False w tablicy is_in_range_A:", ilosc_false)

    