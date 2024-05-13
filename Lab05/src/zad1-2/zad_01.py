# a) 
# Co robi StandardScaler? Jak transformowane są dane liczbowe?

from sklearn.preprocessing import StandardScaler

# Przykładowe dane
data = [[1, 2], [2, 3], [3, 4], [4, 5]]

# Inicjalizacja obiektu StandardScaler
scaler = StandardScaler()

# Dopasowanie scaler do danych i przekształcenie ich
scaled_data = scaler.fit_transform(data)
print("a)")
print("Oryginalne dane:")
print(data)
print("\nPrzekształcone dane:")
print(scaled_data)

# Wniosek: StandardScaler powoduje to żeby średnia każdej wartośći którą przekształcamy dzięki tej funkcji wbudowanej przy pomocy biblioteki była równa 0. Czyli żeby dane wyjściowe miały średnią równą 0, a wariancja wynosiła 1.


# b)
# Czym jest OneHotEncoder (i kodowanie „one hot”ogólnie)? Jak etykiety klas są transformowane przez ten encoder?

from sklearn.preprocessing import OneHotEncoder

# Przykładowe etykiety klas
labels = [[0], [1], [2]]

# Tworzenie obiektu OneHotEncoder
encoder = OneHotEncoder()

# Dopasowanie i przekształcenie etykiet
encoded_labels = encoder.fit_transform(labels).toarray()

# Wyświetlenie przekształconych etykiet
print("\nb)")
print(encoded_labels)


# OneHotEncoder to technika kodowania kategorii, która jest używana do przekształcenia etykiet klas na reprezentację „jednojedynkową” (one-hot). W przypadku problemów klasyfikacji, gdzie mamy wiele klas, zakodowanie „one-hot” polega na przypisaniu unikalnego wektora binarnego dla każdej klasy, gdzie jedna zmienna binarna jest ustawiona na 1 (reprezentuje obecność klasy) i pozostałe są ustawione na 0. Podsumowując, kodowanie „one-hot” zamienia etykiety kategorii na wektory zer i jedynek, gdzie każdy element wektora odpowiada jednej z możliwych kategorii.

# lepszy przykład z np i metodą "one-hot"

from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Przykładowe etykiety klas
labels = np.array(['A', 'B', 'C', 'A', 'C'])

# Tworzenie instancji OneHotEncoder
encoder = OneHotEncoder()

# Dopasowanie etykiet klas i transformacja ich w kodowanie "one-hot"
encoded_labels = encoder.fit_transform(labels.reshape(-1, 1))

# Wyświetlenie ztransformowanych etykiet
print("")
print(encoded_labels.toarray())


# c)
# Model ma 4 warstwy: wejściową, dwie ukryte warstwy z 64 neuronami każda i warstwę wyjściową. Ile neuronów ma warstwa wejściowa i co oznacza X_train.shape[1]? Ile neuronów ma warstwa wyjściowa i co oznacza y_encoded.shape[1]?

# Odp:
# Warstwa wejściowa ma tyle neuronów, ile cech (zmiennych) zawiera każdy przykład danych treningowych. W przypadku tego modelu, X_train.shape[1] oznacza liczbę cech w każdym przykładzie treningowym, czyli ilość kolumn w macierzy danych treningowych X_train.

# Warstwa wyjściowa ma tyle neuronów, ile możliwych klas chcemy przewidzieć. W tym przypadku, y_encoded.shape[1] oznacza liczbę klas, na które kodujemy etykiety klas w formacie „one-hot”.

# Dlatego X_train.shape[1] odpowiada liczbie neuronów warstwy wejściowej, a y_encoded.shape[1] odpowiada liczbie neuronów warstwy wyjściowej.

# d)
# Czy funkcja aktywacji relu jest najlepsza do tego zadania? Spróbuj użyć innej funkcji i obejrzyj wyniki

# Odp:
# Funkcja aktywacji relu jest najlepsza, spróbowałam funkcji aktywacji sigmoid i ma mniejszą dokładność zarówno dla train accurancy jak i validation accurancy.


# e)
# Tak, eksperymentowanie z różnymi optymalizatorami, funkcjami straty i parametrami szybkości uczenia się może prowadzić do różnych wyników treningowych i oceny modelu. Optymalizatory mogą mieć różne sposoby aktualizacji wag modelu, co może wpływać na tempo zbieżności i jakość wyników. Podobnie, różne funkcje straty mają różne sposoby oceny błędu między przewidywaniami a rzeczywistymi etykietami, co może prowadzić do różnych efektów w treningu.


# f)
# W linii model.fit sieć neuronowa jest trenowana. Czy jest sposób, by zmodyfikować tę linię tak, aby rozmiar partii był równy 4 lub 8 lub 16? Jak wyglądają krzywe uczenia się dla różnych parametrów? Jak zmiana partii wpływa na kształt krzywych? Wypróbuj różne wartości i uruchom program

# Odp:
# Tak, możemy zmodyfikować rozmiar partii w linii model.fit poprzez ustawienie parametru batch_size. Aby ustawić rozmiar partii na 4, 8 lub 16, możemy zmienić tę linię na:

# history = model.fit(X_train, y_train, epochs=100, batch_size=4, validation_split=0.2)

# # lub

# history = model.fit(X_train, y_train, epochs=100, batch_size=8, validation_split=0.2)


# # lub

# history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2)

# g)
# Krzywa, która wykazuje niewielkie różnice między wynikami dokładności modelu dla zbioru treningowego i walidacyjnego, sugeruje dobrze dopasowany model. Ponadto, jeśli dokładność dla zbioru treningowego nie osiąga bardzo wysokich wartości (bliskich 100%) podczas ostatnich epok, to również sygnalizuje, że model jest dobrze dopasowany i nie doszło do przeuczenia.

# h)
# Kod jest przykładem uczenia się maszynowego, który wykorzystuje dane irysów do klasyfikacji gatunków. Oto jego wyjaśnienie krok po kroku:

#    - Importowanie niezbędnych bibliotek: numpy do manipulacji danymi, matplotlib do wizualizacji, tensorflow do tworzenia modeli uczenia maszynowego oraz funkcji do wczytywania i przetwarzania danych z biblioteki scikit-learn.

#    - Wczytanie zestawu danych irysów za pomocą funkcji load_iris z modułu datasets z biblioteki scikit-learn. Dane wejściowe (X) zawierają cechy irysów, a etykiety (y) zawierają gatunki irysów.

#    - Przeskalowanie cech danych za pomocą StandardScaler z modułu preprocessing z biblioteki scikit-learn, aby mieć średnią równą zero i jednostkowe odchylenie standardowe.

#    - Zakodowanie etykiet klas irysów za pomocą OneHotEncoder z modułu preprocessing z biblioteki scikit-learn, aby umożliwić reprezentację kategorii jako wektorów zer i jedynek.

#    - Podział zestawu danych na zbiór treningowy i testowy za pomocą funkcji train_test_split z modułu model_selection z biblioteki scikit-learn.

#    - Zdefiniowanie modelu sieci neuronowej za pomocą Sequential z modułu models z biblioteki Keras. Model składa się z trzech warstw gęstych: dwóch warstw ukrytych z aktywacją ReLU i warstwy wyjściowej z aktywacją softmax.

#    - Kompilacja modelu za pomocą funkcji compile. Wybieramy optymalizator 'adam', funkcję straty 'categorical_crossentropy' i metrykę 'accuracy'.

#    - Trenowanie modelu na danych treningowych za pomocą funkcji fit. Przez 100 epok model jest uczony na podstawie danych treningowych, przy użyciu również danych walidacyjnych.

#    - Ocena modelu na zestawie testowym za pomocą funkcji evaluate. Otrzymujemy wyniki straty i dokładności dla zestawu testowego.

#    - Wykresy krzywych uczenia się (dokładności i straty) są tworzone za pomocą matplotlib.

#    - Model jest zapisywany w formacie Keras za pomocą funkcji save.

#    - Architektura modelu jest rysowana i zapisywana jako obraz PNG za pomocą funkcji plot_model.

# Ogólnie rzecz biorąc, kod ten tworzy, trenuje i ocenia model sieci neuronowej do klasyfikacji gatunków irysów na podstawie ich cech.

