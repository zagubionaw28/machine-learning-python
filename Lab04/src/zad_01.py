import pandas as pd
import numpy as np
from math import e as E

df = pd.read_csv("diabetes1.csv")

# print(df)

def forwardPass(wiek,waga,wzrost):
  # def act_func(x):
  #   return 1/(1+E**(-x))


  hidden1 = (-0.46122 * wiek) + 0.80109 + (waga * 0.97314) + (wzrost * -0.39203)
  hidden1_po_aktywacji = (1 / (1+E**-hidden1)) * (-0.81546)
  hidden2 = (wiek * 0.78548) + 0.43529 + (waga * 2.10584) + (wzrost * -0.57847)
  hidden2_po_aktywacji = (1 / (1+E**-hidden2)) * 1.03775
  output = hidden1_po_aktywacji + hidden2_po_aktywacji - 0.2368
  return output


print(forwardPass(23,75,176))
print(forwardPass(25,67,180))
#  = 0.798528



# Epoki - fragment procesu uczenia w którym przeszliśmy dokładnie jeden raz przez każdą próbkę ze zbioru treningowego ucząc się na niej.