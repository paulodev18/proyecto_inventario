inventario = {}
while True:
#este es un comentario para visualizar en github
	nombre = input("Nombre del producto o salir: ")
	if nombre == "salir":
		break
	cantidad = int(input("Cantidad: "))

	if cantidad < 0:
		print ("cantidad inválida, No se agregó el producto.")
	else:
		inventario[nombre] = cantidad
		print ("Producto agregado.")
print ("=== INVENTARIO SUPER  ===")
