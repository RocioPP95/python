print("CONVERTIDOR DE SEGUNDOS A MINUTOS")


segundos = int(input("Escriba una cantidad de segundos: "))

minutos = round(segundos / 60, 2)
restoSegundos = round(segundos % 60, 2)

print(segundos, "segundos son", minutos, "minutos y", restoSegundos, "segundos")
