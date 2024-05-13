import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neural_network import MLPClassifier # neural network
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv("diabetes1.csv")
pd.set_option('future.no_silent_downcasting', True)
sns.pairplot( data=data, vars=('pregnant-times', 'glucose-concentr', 'blood-pressure', 'skin-thickness', "insulin", 'mass-index', 'pedigree-func', 'age'), hue='class')

#b) i c)
target = data[['class']].replace(['tested_positive', 'tested_negative'],[1,0]).infer_objects()
df = data[['pregnant-times', 'glucose-concentr', 'blood-pressure', 'skin-thickness', 'insulin', 'mass-index', 'pedigree-func', 'age']]

X = df[['pregnant-times', 'glucose-concentr', 'blood-pressure', 'skin-thickness', 'insulin', 'mass-index', 'pedigree-func', 'age']]
Y = target['class']

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3, random_state=285763)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(6, 3), random_state=1, max_iter=500, activation = 'relu')
#fit - funkcja trenująca
clf.fit(trainX, trainY)
#d)
# Przewidywanie etykiet dla danych testowych
predicted_labels = clf.predict(testX)
# Obliczanie dokładności
accuracy = accuracy_score(testY, predicted_labels)


# Macierz błędu
conf_matrix = confusion_matrix(testY, predicted_labels)

# Wyświetlanie macierzy błędu
print("Confusion Matrix:")
print(conf_matrix)

#e)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(7, 3, 3), random_state=1, max_iter=500, activation = 'logistic')
#fit - funkcja trenująca
clf.fit(trainX, trainY)
# Przewidywanie etykiet dla danych testowych
predicted_labels = clf.predict(testX)
# Obliczanie dokładności
accuracy = accuracy_score(testY, predicted_labels)
print(accuracy)
print(testY)


# Macierz błędu
conf_matrix = confusion_matrix(testY, predicted_labels)

# Wyświetlanie macierzy błędu
print("Confusion Matrix:")
print(conf_matrix)

# Tworzenie heatmapy
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g', 
            xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# FP = 33
# FN = 54
# Gorsze błędy to false negative.