month=dict(
    Enero=1,
    Febrero=2,
    Marzo=3,
    Abril=4,
    Mayo=5,
    Junio=6,
    Julio=7,
    Agosto=8,
    Septiembre=9,
    Octubre=10,
    Noviembre=11,
    Diciembre=12,
)
total=0


for clave, valor in month.items():

    max_values=max(month, key=month.get)
    
print('El mes con mayor produccion es: ',max_values,' y su valor es  ', month[max_values])

for clave, valor in month.items():

    min_values=min(month, key=month.get)
    
print('El mes con menor produccion es: ',min_values,' y su valor es  ', month[min_values])

for i in month.values():
    total += i
promedio= total/12

print('El valor promedio es: ',promedio)

for key in month.keys():
    if month[key]<= promedio:
        print('Los meses por encima del promedio son: ', key)

for key in month.keys():
    if month[key]>= promedio:
        print('Los meses por debajo del promedio son: ', key)

