import datetime
import math

aktualna_data = datetime.datetime.now()
rokTeraz = aktualna_data.year
dzienTeraz = aktualna_data.day
miesiacTeraz = aktualna_data.month

imie = input("Jak masz na imię? ")

rok = int(input("W jakim roku się urodziłeś? "))
while rok < 1000 or rok > rokTeraz:
    print("Podano błędny rok.")
    rok = int(input("W którym roku się urodziłeś? "))

miesiac = int(input("W jakim miesiącu się urodziłeś? "))
while miesiac < 1 or miesiac > 12:
    print("Podano błędny miesiąc.")
    miesiac = int(input("W jakim miesiącu się urodziłeś? "))

dzien = int(input("W jakim dniu się urodziłeś? "))
while dzien < 1 or dzien > 31 or (miesiac == 2 and dzien > 29 and rok % 4 == 0) or \
        (miesiac == 2 and dzien > 28 and rok % 4 != 0) or \
        ((miesiac in [4, 6, 9, 11]) and dzien > 30):
    print("Podano błędny dzień.")
    dzien = int(input("W jakim dniu się urodziłeś? "))

liczba_dni = (datetime.date(rokTeraz, miesiacTeraz, dzienTeraz) - datetime.date(rok, miesiac, dzien)).days

print("Witaj, miło Cię poznać, " + imie + "!")
print("Dzisiaj jest Twój " + str(liczba_dni) + " dzień życia.")

# Fizyczna Fala
y_p = math.sin(2 * math.pi * liczba_dni / 23)
print("Fizyczna Fala:", y_p)

# Emocjonalna Fala
y_e = math.sin(2 * math.pi * liczba_dni / 28)
print("Emocjonalna Fala:", y_e)

# Intelektualna Fala
y_i = math.sin(2 * math.pi * liczba_dni / 33)
print("Intelektualna Fala:", y_i)

# Fizyczna Fala dzień następny
y_p_2 = math.sin(2 * math.pi * (liczba_dni + 1) / 23)

# Emocjonalna Fala dzień następny
y_e_2 = math.sin(2 * math.pi * (liczba_dni + 1) / 28)

# Intelektualna Fala dzień następny
y_i_2 = math.sin(2 * math.pi * (liczba_dni + 1) / 33)

print("---------------------------------------")
if y_p > 0.5:
    print("Dobry wynik Fizycznej Fali")
elif y_p_2 > 0.5:
    print("Nie martw się. Jutro będzie lepiej w Fizycznej Fali!")
else:
    print("Następnym razem będzie lepiej w Fizycznej Fali")

if y_e > 0.5:
    print("Dobry wynik Emocjonalnej Fali")
elif y_e_2 > 0.5:
    print("Nie martw się. Jutro będzie lepiej w Emocjonalnej Fali!")
else:
    print("Następnym razem będzie lepiej w Emocjonalnej Fali")

if y_i > 0.5:
    print("Dobry wynik Intelektualnej Fali")
elif y_i_2 > 0.5:
    print("Nie martw się. Jutro będzie lepiej w Intelektualnej Fali!")
else:
    print("Następnym razem będzie lepiej w Intelektualnej Fali")
