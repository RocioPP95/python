print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")

# Pedir los datos al usuario
peso = float(input("¿Cuánto pesa? "))
altura = float(input("¿Cuánto mide en metros? "))


imc = peso / (altura ** 2)


print("Su imc es", round(imc, 2))

# Información adicional
print("Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,pero esos límites dependen de la edad, del sexo, de la constitución física, etc.")

