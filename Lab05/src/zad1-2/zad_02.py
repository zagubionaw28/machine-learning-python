# a) W preprocessingu:

#    - reshape: Zmienia kształt tablicy danych, aby pasowała do oczekiwanego kształtu wejściowego dla sieci neuronowej. W tym przypadku, obrazy 28x28 są przekształcane do tablicy 28x28x1, aby pasowały do oczekiwanego kształtu wejściowego dla warstwy konwolucyjnej.
#    - to_categorical: Przekształca etykiety klas na postać kodowania „one-hot”, co jest wymagane do treningu modelu klasyfikacji wieloklasowej.
#    - np.argmax: Zwraca indeksy maksymalnych wartości w tablicy. W tym przypadku, używany jest do przekształcenia zakodowanych etykiet z powrotem na ich pierwotne wartości przedstawiające klasy.

# b) Dane przechodzą przez sieć neuronową od warstw wejściowych do warstw wyjściowych. W przypadku tego modelu:

#    - Dane obrazów 28x28x1 są przekazywane do warstwy konwolucyjnej, która wykrywa lokalne wzorce w obrazach za pomocą filtrów konwolucyjnych.
#    - Wyniki z warstwy konwolucyjnej przechodzą przez warstwę MaxPooling, która zmniejsza rozmiar przestrzenny danych poprzez wybieranie maksymalnej wartości z określonych regionów.
#    - Wyjście z warstwy MaxPooling jest spłaszczane do wektora i przekazywane do warstwy w pełni połączonej, gdzie odbywa się dalsza analiza danych.
#    - Na końcu, wyjście z warstwy w pełni połączonej przechodzi przez warstwę wyjściową, która przewiduje prawdopodobieństwo każdej z 10 klas.

# c) Najwięcej błędów w macierzy błędów występuje na przekątnej, co oznacza, że modele poprawnie przewidują większość klas. Często jednak cyfry są mylone z innymi w miarę podobnymi kształtami, takimi jak 7 z 9 lub 3 z 5.

# d) Krzywe uczenia sugerują, że model nie ulega ani przeuczeniu, ani niedouczeniu się. Krzywa dokładności trenowania i walidacji zbliża się do siebie, co oznacza, że model generalizuje dobrze dla zbioru walidacyjnego.

# e) Aby zapisać model do pliku .h5 co epokę, pod warunkiem, że osiągnięto lepszy wynik, możesz użyć funkcji callback ModelCheckpoint w Kerasie. 
# Zmodyfikowany kod:
from tensorflow.keras.callbacks import ModelCheckpoint

# Define checkpoint callback
checkpoint = ModelCheckpoint(filepath='model_{epoch:02d}.h5', 
                             monitor='val_accuracy', 
                             verbose=1, 
                             save_best_only=True, 
                             mode='max')

# Train model with checkpoint callback
history = model.fit(train_images, train_labels, 
                    epochs=5, 
                    batch_size=64, 
                    validation_split=0.2, 
                    callbacks=[history, checkpoint])
