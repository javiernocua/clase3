#reto 4
cajas_refresco=int(input("Ingrese cantidad de cajas: "))
unidades_caja=int(input("Ingrese unidades por caja: " ))
personas=int(input("Ingrese cantidad de personas: " ))
cantidad_refrescos=cajas_refresco*unidades_caja
sobrante=cantidad_refrescos%personas
print("La cantidad de refrescos sobrantes es:",sobrante)