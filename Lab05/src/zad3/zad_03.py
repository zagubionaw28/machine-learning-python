import sys

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization
from keras.optimizers import Adam
from keras.callbacks import History
from tensorflow.math import confusion_matrix
from keras.utils import image_dataset_from_directory
from keras.models import Sequential



DATASET_DIR = "data-cats-dogs/"


def train_model(train_data, validation_data, batch_size, input_shape):
    
    model = create_model(input_shape)
    history = History()
    model.fit(train_data, validation_data=validation_data, epochs=5, batch_size=batch_size, validation_split=0.2, callbacks=[history])
    # dane treningowe (train_data), dane walidacyjne (validation_data), liczbę epok (w tym przypadku 5), rozmiar partii (batch_size), ułamek danych treningowych używanych jako walidacyjne (validation_split=0.2) oraz listę zwrotnych wywołań (callbacks), w tym przypadku obiekt history.
    cm = calculate_confusion_matrix(model, validation_data)
    # Oblicza macierz pomyłek (confusion matrix) na podstawie modelu i danych walidacyjnych przy użyciu funkcji
    plot_diagnostics(history, cm)

def plot_diagnostics(history, cm):
    # plot confusion matrix
    plt.figure(figsize=(10, 7))
    # Tworzy nową figurę Matplotlib o rozmiarze 10x7 cali. Ta figura będzie zawierać wykres macierzy pomyłek.
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    # Tworzy mapę ciepła (heatmap) dla macierzy pomyłek cm za pomocą biblioteki Seaborn. Mapa ciepła jest używana do wizualizacji danych w postaci kolorowej siatki, gdzie każdy kolor odpowiada wartości w macierzy pomyłek. Parametr annot=True oznacza, że liczby będą wyświetlane w komórkach mapy ciepła, fmt='d' oznacza, że liczby będą wyświetlane jako liczby całkowite, a cmap='Blues' określa paletę kolorów.
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.savefig("confusion_matrix.png")

    # plot training and validation accuracy
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    # Tworzy pierwszy podwykres w siatce 1x2. To oznacza, że nasza figura będzie zawierać dwie kolumny, a ten podwykres będzie znajdować się w pierwszej kolumnie.
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
		# Dodaje etykietę do osi x, która oznacza liczby epok.
    plt.ylabel('Accuracy')
    plt.grid(True, linestyle='--', color='grey')
    # Dodaje siatkę na wykresie dla łatwiejszego odczytu.
    plt.legend()

    # plot training and validation loss
    plt.subplot(1, 2, 2)
    # Tworzy drugi podwykres w tej samej siatce 1x2. To oznacza, że ten podwykres będzie znajdować się w drugiej kolumnie.
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True, linestyle='--', color='grey')
    plt.legend()

    plt.tight_layout()
    plt.savefig("accuracy.png")


def create_model(input_shape):
    model = Sequential()
    # Tworzy nowy model sekwencyjny za pomocą klasy Sequential z Kerasa. Model ten jest liniowym stosowaniem warstw.
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(*input_shape, 3)))
    # Dodaje warstwę konwolucyjną 2D do modelu. Ta warstwa używa 32 filtrów o rozmiarze 3x3, funkcji aktywacji ReLU, strategii inicjalizacji wag 'he_uniform' oraz takiego samego dopełnienia ('same'), co oznacza, że wyjście będzie miało taki sam rozmiar jak wejście. Parametr input_shape określa kształt wejścia.

    model.add(Conv2D(64, (3, 3), activation='relu'))
    # Dodaje kolejną warstwę konwolucyjną 2D z 64 filtrami o rozmiarze 3x3 i funkcją aktywacji ReLU. W tej warstwie nie określono strategii inicjalizacji wag ani dopełnienia, co oznacza, że zostaną one użyte wartości domyślne.
    model.add(BatchNormalization())
    # Dodaje warstwę normalizacji wsadowej (Batch Normalization), która normalizuje aktywacje poprzedniej warstwy w sposób, który przyspiesza trening i zmniejsza wrażliwość na inicjalizację wag.
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Dodaje warstwę poolingową MaxPooling 2D z rozmiarem okna 2x2. Ta warstwa zmniejsza wymiarowość przestrzenną danych poprzez pobieranie maksymalnej wartości z okna o określonym rozmiarze.
    model.add(Dropout(0.25))
    # Dodaje warstwę Dropout z wartością 0.25, co oznacza, że losowo wyłącza 25% neuronów w warstwie podczas treningu w celu zapobiegania nadmiernemu dopasowaniu.

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    # Dodaje warstwę Flatten, która przekształca dane wejściowe z formatu tensora wielowymiarowego na format jednowymiarowy, aby mogły być przekazane do warstw w pełni połączonych.
    model.add(Dense(256, activation='relu', kernel_initializer='he_uniform'))
    # Dodaje warstwę Dense (w pełni połączoną) z 256 neuronami, funkcją aktywacji ReLU i strategią inicjalizacji wag 'he_uniform'.
    model.add(Dense(1, activation='sigmoid'))
    # Dodaje warstwę Dense z jednym neuronem i funkcją aktywacji sigmoidalną. Ta warstwa służy do klasyfikacji binarnej, gdzie wartość sigmoidalna zwraca prawdopodobieństwo przynależności do jednej z dwóch klas.
    # compile model
    opt = Adam(learning_rate=0.001)
    # Tworzy optymalizator Adam z określoną szybkością uczenia.
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model


def calculate_confusion_matrix(model, validation_data):
    true_labels = []
    # Tworzy pustą listę true_labels, która będzie przechowywać prawdziwe etykiety danych walidacyjnych (zbiór testowy)
    for _, labels in validation_data:
        true_labels.extend(labels.numpy())
        # Rozszerza listę true_labels o prawdziwe etykiety z danych walidacyjnych. labels.numpy() konwertuje tensor TensorFlow na tablicę numpy, co umożliwia łatwe połączenie etykiet z innymi etykietami.

    predicted_probs = model.predict(validation_data)
    # Przewiduje etykiety dla danych walidacyjnych za pomocą funkcji predict modelu. Zwraca prawdopodobieństwa przewidywane przez model dla każdej klasy.
    predicted_classes = np.where(predicted_probs > 0.5, 1, 0)
    # Tworzy tablicę przewidzianych klas na podstawie prawdopodobieństw przewidywanych przez model. Jeśli prawdopodobieństwo przewidywanej klasy jest większe niż 0,5, przypisuje klasę 1, w przeciwnym razie przypisuje klasę 0.

    cm = confusion_matrix(true_labels, predicted_classes)
    # Oblicza macierz pomyłek (confusion matrix) na podstawie prawdziwych etykiet i przewidywanych klas.
    return cm
     

if __name__ == "__main__":
    image_size = (50, 50)
    batch_size = 8

    train_data = image_dataset_from_directory(
      DATASET_DIR,
      validation_split=0.2,
      # Tworzy zbiór danych walidacyjnych validation_data w sposób podobny do zbioru treningowego, ale z innym podziałem na dane walidacyjne.
      subset="training",
      seed=288498,
      image_size=image_size,
      batch_size=batch_size
      # Określa rozmiar partii danych, które będą przetwarzane jednocześnie podczas uczenia modelu.
    )

    validation_data = image_dataset_from_directory(
      DATASET_DIR,
      validation_split=0.2,
      subset="validation",
      seed=288498,
      image_size=image_size,
      batch_size=batch_size
    )

    train_model(train_data, validation_data, batch_size, image_size)
