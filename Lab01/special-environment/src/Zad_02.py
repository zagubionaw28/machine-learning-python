import random
import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # Przyspieszenie ziemskie w m/s^2
h = 100  # Wysokosc w metrach

def sprawdz_trafienie(odleglosc, predkosc, kat, margines_bledu):
    # Kontrola, aby uniknąć kątów równych 90 stopni
    if kat >= 90 or kat <= 0:
        return False
    # Obliczanie zasiegu rzeczywistego na podstawie kata
    zasieg_rzeczywisty = (predkosc * math.sin(math.radians(kat)) + math.sqrt(predkosc**2 * math.sin(math.radians(kat))**2 + 2 * g * h)) * predkosc * math.cos(math.radians(kat)) / g

    # print(zasieg_rzeczywisty45)
    # Sprawdzenie trafienia z uwzglednieniem marginesu bledu
    if abs(zasieg_rzeczywisty - odleglosc) <= margines_bledu:
        return True
    else:
        return False


odleglosc_celu = random.randint(50, 340)
print("Cel znajduje się w odległości:", odleglosc_celu, "metrów")

v = 50  # Predkosc w m/s

liczba_prob = 0

while True:
    kat_strzalu = float(input("Podaj kąt strzału w stopniach (od 0 do 89): "))
    if kat_strzalu < 0 or kat_strzalu > 89:
        print("Błąd! Kąt strzału musi być pomiędzy 0 a 89 stopni.")
        continue  # Ponowne wyświetlenie zapytania o kąt strzału
    liczba_prob += 1
    
    if sprawdz_trafienie(odleglosc_celu, v, kat_strzalu, 5):
        print("Cel trafiony!")
        print("Całkowita liczba prób strzału:", liczba_prob)
        break
    else:
        print("Pocisk chybił celu. Spróbuj ponownie.")
        zasieg_rzeczywisty = (v * math.sin(math.radians(kat_strzalu)) + math.sqrt(v**2 * math.sin(math.radians(kat_strzalu))**2 + 2 * g * h)) * v * math.cos(math.radians(kat_strzalu)) / g
        print(zasieg_rzeczywisty)

# Dane

margines_bledu = 5  # Margines błędu w metrach

# Konwersja kąta na radiany
kat_radiany = np.radians(kat_strzalu)

# Obliczenie składowych prędkości początkowej
v0x = v * np.cos(kat_radiany)
v0y = v * np.sin(kat_radiany)

# Obliczenie czasu lotu
czas_lotu = (2* v0y)/g + 3.5
# 2 *v*math.sin(kat_radiany)/g + 3

# Stworzenie tablicy czasu
czas_tablica = np.linspace(0, czas_lotu, 100)

# def trajectory(x):
#     return h + v0y * czas_tablica - 0.5 * g * czas_tablica ** 2
# Obliczenie położenia pocisku w czasie
x = v0x * czas_tablica
y = h + v0y * czas_tablica - 0.5 * g * czas_tablica ** 2  # Dodanie wysokości początkowej h do położenia w osi Y

# Rysowanie trajektorii
plt.plot(x, y, 'b-', label='Trajektoria pocisku')

# Rysowanie końcowego położenia pocisku
plt.plot(odleglosc_celu, 0, 'go', label='Końcowe położenie')

# # Rysowanie linii końcowej wysokości
# plt.plot([x[-1], odleglosc_celu], [y[-1], 0], 'b-')

    # Rysowanie celu
plt.plot([odleglosc_celu - margines_bledu, odleglosc_celu + margines_bledu], [h, h], 'r-', linewidth=3)  # Dodanie wysokości początkowej h do położenia celu

# Ustawienie limitów osi x i y
plt.xlim(0, 340)
plt.ylim(0, 300)

# Konfiguracja wykresu
plt.xlabel('Odległość [m]')
plt.ylabel('Wysokość [m]')
plt.title('Trajektoria pocisku Warwolf')
plt.grid(True)

# Zapisanie wykresu do pliku
plt.savefig('trajektoria.png')

# Wyświetlenie wykresu
plt.show()
