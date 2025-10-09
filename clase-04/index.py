daysOfWeek = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
highTemperatures = []
allTemperatures = []

print("-----------------------PROGRAMA DE TEMPERATURA-----------------------")

for (index, day) in enumerate(daysOfWeek):
    print(f"{index+1}. {day}")

print("Seleccione 5 dias de la semana para ingresar la temperatura:")
for i in range(5):
    daySelected = int(input(f"Selecciona el dia {i + 1}: ")) - 1
    if 0 <= daySelected < len(daysOfWeek):
        temperature = float(input(f"Ingrese la temperatura para {daysOfWeek[daySelected]}: "))
        highTemperatures.append(temperature) if temperature > 25 else None
        allTemperatures.append(temperature)
    else:
        print("Número de día inválido. Por favor, intente de nuevo.")

print("Temperaturas altas (mayores a 25°C):", highTemperatures)
print("Temperatura promedio:", sum(highTemperatures) / len(highTemperatures) if highTemperatures else 0)
print("Resumen de temperaturas ingresadas:")
for i in allTemperatures:
    print(f"Temperatura: {i}°C")

print("Gracias por usar el programa de temperatura.")
print("---------------------------------------------------------------------")
