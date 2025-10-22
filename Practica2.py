print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")

# Pedir los datos al usuario
peso = float(input("¿Cuánto pesa? "))
altura = float(input("¿Cuánto mide en metros? "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado redondeado a un decimal
print("Su imc es", round(imc, 1))

# Información adicional
print("Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,pero esos límites dependen de la edad, del sexo, de la constitución física, etc.")

