#def refrescos_sobrante():
    #cajas_refresco=int(input("Ingrese cantidad de cajas: "))
    #unidades_caja=int(input("Ingrese unidades por caja: " ))
    #personas=int(input("Ingrese cantidad de personas: " ))
    #cantidad_refrescos=cajas_refresco*unidades_caja
    #sobrante=cantidad_refrescos%personas
    #print("La cantidad de refrescos sobrantes es:",sobrante)

def refrescos_sobrante(unidades_caja, cajas_refresco, personas):
    cantidad_refrescos=cajas_refresco*unidades_caja
    sobrante=cantidad_refrescos%personas
    return sobrante 

#cajas_refresco=int(input("Ingrese cantidad de cajas: "))
#unidades_caja=int(input("Ingrese unidades por caja: " ))
#personas=int(input("Ingrese cantidad de personas: " ))
#refrescos_sobrante(unidades_caja, cajas_refresco, personas)
#refrescos_sobrante(24, 9, 56)
#print("La cantidad de refrescos sobrantes es:",sobrante)

var_1=refrescos_sobrante(24,9,56)
print("La cantidad de refrescos sobrantes es: ",var_1)


def precio_por_kilo(peso_empaque, precio_empaque, peso_kilo=1000):
    #peso_kilo= 1000
    precio_gramo= precio_empaque/peso_empaque
    precio_kilo= precio_gramo*peso_kilo
    return round(precio_kilo,2)

#peso_empaque=float(input("Ingrese peso de empaque: "))
#precio_empaque=float(input("Ingrese precio de empaque: "))
#var_1=precio_por_kilo(peso_empaque, precio_empaque)
var_1=precio_por_kilo(100, 5.95)
print("el precio por kilo es: ",var_1)
print("el precio por kilo es: ", precio_por_kilo(100, 5.95))
print("el precio por kilo es: ", precio_por_kilo(100, 5.95, 2000))

#precio_por_kilo()