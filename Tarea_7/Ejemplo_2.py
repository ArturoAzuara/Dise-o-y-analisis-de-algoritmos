monedas = [1, 2, 5]
S = 10
total = []

for i in range(len(monedas)):
    for j in range(len(monedas)):
        suma = sum([monedas[i], monedas[j]])
        total.append(suma)

sublista = [total[i:i + 3] for i in range(0, len(total), 3)]

mejor_combinacion = None
sobrante = None

for combinacion in sublista:
    combinacion_suma = sum(combinacion)
    if sum(combinacion) >= S:
        mejor_combinacion = combinacion
        sobrante = combinacion_suma - S
        break
if mejor_combinacion is not None:
    print(f"La mejor combinación es: {mejor_combinacion}, con un sobrante de {sobrante}")
else:
    print("No hay manera de tener una combinacion proxima a lo solicitado")
