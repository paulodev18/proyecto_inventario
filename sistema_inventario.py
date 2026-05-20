nombre = input("Nombre del producto: ")
cantidad = int(input("Cantidad: "))
#print("Producto:", nombre, "Cantidad:", cantidad)

if cantidad < 0:
	print ("la cantidad no puede ser negativa")
else:
	print ("Producto: ",nombre, " Cantidad: ",cantidad)
