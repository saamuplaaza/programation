producto=input("Nombre del producto: ")
precio=input("Precio/unidad: ")
unidades=float(input("Unidades: "))
precio=float(precio).__round__(2)
print("%s:%s€, %s unidades. Total=%s€"%(producto,precio,unidades,precio*unidades))