# Zadanie jest następujące:
# a)Napisz program w Pythonie, który spyta użytkownika oimię, rok urodzenia, miesiąc urodzenia i dzień urodzenia. Następnie wita użytkownika, informuje go, który dzień ich życia jest dzisiaj, oblicza ich fizyczne, emocjonalne i intelektualne wyniki biorytmów i drukuje je. Jeśli to możliwe, zrób to bez użycia narzędzi AI. Możesz korzystać z zasobów online. Sprawdź swój biorytm! Jak się czujesz dzisiaj? 
# b)Zmodyfikuj swój program. Po obliczeniu biorytmów program powinien sprawdzić, czy są one wysokie (powyżej 0,5) i pogratulować dobrego wyniku, niskie (mniejsze niż -0,5) i pocieszyć w złym dniu. W przypadku niskiego wyniku algorytm sprawdza również, czy następny dzień przyniesie wyższy czy niższy wynik.W przypadku wyższego wyniku program powinien powiedzieć coś w rodzaju „Nie martw się. Jutro będzie lepiej!”
# c)Zmierz (mniej więcej) ile czasu spędziłeś/aśna pisaniu programu (a-b), łącznie z badaniami online. Napisz swoją odpowiedź jako komentarz w programie.
# d)Poproś ChatGPT lub inne narzędzie AI o korektę programu, lub poprawę stylistyczną. Zapisz kopię programu.
# e)Zacznij nową, czystą rozmowę z ChatGPT1(lub innym narzędziem) i spróbuj poprosić o kompletny program. Zobacz, czy ChatGPT będzie w stanie napisać program samodzielnie. Musisz skonstruować swoje polecenie w dobry, jasny, precyzyjny sposób, aby zrozumiał zadanie. Zmierz, ile czasu spędziłeś/aśna uzyskaniu poprawnego programu (czy zajęło to więcej czasu niż w punkcie (c)?)

import datetime
from datetime import date
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


dzien = int(input("W jakim dniu się urodziłeś "))
while dzien < 1 or dzien > 31 or (miesiac == 2 and dzien > 29 and rok%4 == 0) or (miesiac == 2 and dzien > 28 and rok%4 != 0) or ((miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11) and dzien > 30 ):
  print("Podano błędny dzien.")
  dzien = int(input("W jakim dniu się urodziłeś "))

liczba_dni = (date(rokTeraz, miesiacTeraz, dzienTeraz) - date(rok, miesiac, dzien)).days

print("Witaj, miło Cię poznać " + imie + "!")
print("Dzisiaj jest twój " + str(liczba_dni) + " dzień życia")

# Fizyczna Fala

y_p = math.sin(int(2 * int(math.pi) * liczba_dni) / 23)

print("Fizyczna Fala:", y_p)

# Emocjonalna Fala
y_e = math.sin(int(2 * int(math.pi) * liczba_dni) / 28)

print("Emocjonalna Fala:", y_e)

# Intelektualna Fala
y_i = math.sin(int(2 * int(math.pi) * liczba_dni) / 33)

print("Intelektualna Fala:", y_i)

# Fizyczna Fala dzień następny

y_p_2 = math.sin(int(2 * int(math.pi) * (liczba_dni+1)) / 23)

# Emocjonalna Fala dzień następny
y_e_2 = math.sin(int(2 * int(math.pi) * (liczba_dni+1)) / 28)
print("Emocjonalna Fala ++++++:", y_e_2)

# Intelektualna Fala dzień następny
y_i_2 = math.sin(int(2 * int(math.pi) * (liczba_dni+1)) / 33)

print("---------------------------------------")
if (y_p > 0.5): 
  print("Dobry wynik Fizycznej Fali")
elif (y_p_2 > 0.5): 
  print("Nie martw się. Jutro będzie lepiej w Fizycznej Fali!")
else: 
  print("Następnym razem będzie lepiej w Fizycznej Fali")

if (y_e > 0.5): 
  print("Dobry wynik Emocjonalnej Fali")
elif (y_e_2 > 0.5):
   print("Nie martw się. Jutro będzie lepiej w Emocjonalnej Fali!")
else: 
  print("Następnym razem będzie lepiej w Emocjonalnej Fali")

if (y_i > 0.5): 
  print("Dobry wynik Intelektualnej Fali")
elif (y_i_2 > 0.5): 
  print("Nie martw się. Jutro będzie lepiej w Intelektualnej Fali!")
else: 
  print("Następnym razem będzie lepiej w Intelektualnej Fali")

# c) Zajęło mi to tak z 5H
# e) Zajeło to z 5 min