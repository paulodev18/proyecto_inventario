# ============================================
# SISTEMA DE INVENTARIO - VERSIÓN FINAL
# Módulos organizados por tipo de estructura
# ============================================

# ============================================
# 1. MÓDULOS CON ESTRUCTURA SECUENCIAL
# ============================================

def mostrar_bienvenida():
    """Secuencial: muestra mensaje de bienvenida"""
    print("=" * 50)
    print("   SISTEMA DE INVENTARIO - VERSIÓN FINAL")
    print("=" * 50)
    print("Este sistema te permite gestionar tu inventario")
    print("de manera modular y organizada")
    print("=" * 50)

def mostrar_despedida():
    """Secuencial: muestra mensaje de despedida"""
    print("\n" + "=" * 50)
    print("   GRACIAS POR USAR EL SISTEMA")
    print("=" * 50)

# ============================================
# 2. MÓDULOS CON ESTRUCTURA CONDICIONAL
# ============================================

def validar_cantidad(cantidad):
    """
    Condicional (if-elif-else): valida si cantidad es válida
    Retorna: (es_valida, mensaje)
    """
    if cantidad > 0:
        return True, "Cantidad válida"
    elif cantidad == 0:
        return False, "La cantidad no puede ser cero"
    else:
        return False, "La cantidad no puede ser negativa"

def validar_producto_existe(inventario, nombre):
    """Condicional simple (if-else): verifica si un producto existe"""
    if nombre in inventario:
        return True
    else:
        return False

def procesar_agregado(inventario, nombre, cantidad):
    """
    Condicionales anidadas: procesa el agregado de un producto
    Retorna: (inventario_actualizado, mensaje)
    """
    es_valida, mensaje = validar_cantidad(cantidad)
    
    if not es_valida:
        return inventario, f"✗ Error: {mensaje}"
    
    # Condicional anidada (dentro de otra condicional)
    if nombre in inventario:
        inventario[nombre] += cantidad
        return inventario, f"✓ Se sumaron {cantidad} a '{nombre}'. Total: {inventario[nombre]}"
    else:
        inventario[nombre] = cantidad
        return inventario, f"✓ Producto '{nombre}' agregado con {cantidad} unidades"

# ============================================
# 3. MÓDULOS CON ESTRUCTURA REPETITIVA
# ============================================

def agregar_productos_multiple(inventario):
    """
    Repetitiva (while): permite agregar varios productos seguidos
    El usuario decide cuándo terminar
    """
    print("\n--- MODO AGREGAR MÚLTIPLES PRODUCTOS ---")
    print("Escribe 'fin' en el nombre para terminar\n")
    
    while True:
        nombre = input("Nombre del producto: ").lower()
        
        if nombre == 'fin':
            break
        
        cantidad = int(input("Cantidad: "))
        inventario, mensaje = procesar_agregado(inventario, nombre, cantidad)
        print(mensaje)
    
    return inventario

def mostrar_inventario(inventario):
    """
    Repetitiva (for): recorre y muestra todos los productos
    """
    print("\n" + "=" * 50)
    print("   INVENTARIO ACTUAL")
    print("=" * 50)
    
    if len(inventario) == 0:
        print("   El inventario está vacío")
    else:
        # Bucle for para iterar sobre el diccionario
        for producto, cantidad in inventario.items():
            print(f"   • {producto}: {cantidad} unidades")
    
    print("=" * 50)

def eliminar_producto_multiple(inventario):
    """
    Repetitiva (while): permite eliminar varios productos
    """
    print("\n--- MODO ELIMINAR PRODUCTOS ---")
    print("Escribe 'fin' para terminar\n")
    
    while True:
        nombre = input("Nombre del producto a eliminar: ").lower()
        
        if nombre == 'fin':
            break
        
        if validar_producto_existe(inventario, nombre):
            del inventario[nombre]
            print(f"✓ Producto '{nombre}' eliminado")
        else:
            print(f"✗ Producto '{nombre}' no encontrado")
    
    return inventario

# ============================================
# 4. MÓDULO DEL MENÚ (combina secuencial + condicional)
# ============================================

def mostrar_menu():
    """Secuencial: muestra las opciones del menú"""
    print("\n" + "-" * 40)
    print("   MENÚ PRINCIPAL")
    print("-" * 40)
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Eliminar productos")
    print("4. Salir")
    print("-" * 40)

def ejecutar_menu():
    """
    Condicional múltiple (if-elif-else) + bucle while
    Controla el flujo principal del programa
    """
    inventario = {}
    mostrar_bienvenida()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            inventario = agregar_productos_multiple(inventario)
        
        elif opcion == "2":
            mostrar_inventario(inventario)
        
        elif opcion == "3":
            inventario = eliminar_producto_multiple(inventario)
        
        elif opcion == "4":
            mostrar_despedida()
            break
        
        else:
            print("✗ Opción no válida. Por favor elige 1, 2, 3 o 4")

# ============================================
# 5. PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal que inicia el programa"""
    ejecutar_menu()

# Punto de entrada
if __name__ == "__main__":
    main()
