import datetime

def daysCalculation(year, month, day):
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    days = (today - birthday).days
    return days

rok_urodzenia = 1500
miesiac_urodzenia = 4
dzien_urodzenia = 1

ile_dni = daysCalculation(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)

print("Masz", ile_dni, "dni.")
