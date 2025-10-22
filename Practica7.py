print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")

segundos = int(input("Escriba una cantidad de segundos: "))

horas = round(segundos / 3600, 2)
minutos = round((segundos % 3600) / 60, 2)
resto_segundos = round(segundos % 60, 2)

print(segundos, "segundos son", horas, "horas,", minutos, "minutos y", restoSegundos, "segundos")
