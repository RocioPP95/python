print("CONVERTIDOR A GRUESAS Y DOCENAS")

cantidad = int(input("Escriba una cantidad (entera): "))

gruesas = round(cantidad / 144, 2)
docenas = round((cantidad % 144) / 12, 2)
unidades = round(cantidad % 12, 2)

print(cantidad, "unidades son", gruesas, "gruesas,", docenas, "docenas y", unidades, "unidades")