#ejercicio 2
peso_empaque=float(input("Ingrese peso de empaque: "))
precio_empaque=float(input("Ingrese precio de empaque: "))
peso_kilo= 1000
precio_gramo= precio_empaque/peso_empaque
precio_kilo= precio_gramo*peso_kilo
print("el precio por kilo es:",precio_kilo)