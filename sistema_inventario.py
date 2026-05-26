# ============================================
# SISTEMA DE INVENTARIO - VERSIÓN MODULAR COMPLETA
# Conceptos: Secuencial + Condicional + Repetitivo (while/for)
# ============================================

# ---------- MÓDULO 1: ESTRUCTURA SECUENCIAL ----------
def mostrar_bienvenida():
    """Muestra mensaje de bienvenida (secuencial)"""
    print("=" * 50)
    print("   SISTEMA DE INVENTARIO - VERSIÓN MODULAR")
    print("=" * 50)

# ---------- MÓDULO 2: ESTRUCTURA CONDICIONAL ----------
def validar_cantidad(cantidad):
    """Valida si una cantidad es válida (condicional if-elif-else)"""
    if cantidad > 0:
        return True, "Cantidad válida"
    elif cantidad == 0:
        return False, "La cantidad no puede ser cero"
    else:
        return False, "La cantidad no puede ser negativa"

# ---------- MÓDULO 3: ESTRUCTURA REPETITIVA (while) ----------
def agregar_multiple_productos():
    """
    Permite agregar varios productos usando un bucle while
    El usuario decide cuándo terminar escribiendo 'fin'
    """
    inventario = {}  # Diccionario vacío para guardar productos
    contador = 0     # Contador para mostrar cuántos se agregaron
    
    print("\n--- AGREGAR PRODUCTOS ---")
    print("Escribe 'fin' para terminar\n")
    
    while True:  # Bucle infinito controlado por break
        nombre = input("Nombre del producto: ").lower()
        
        # Condicional para salir del bucle
        if nombre == 'fin':
            break
        
        cantidad = int(input("Cantidad: "))
        
        # Usar el módulo condicional de validación
        es_valida, mensaje = validar_cantidad(cantidad)
        
        if es_valida:
            # Si el producto ya existe, sumar cantidad
            if nombre in inventario:
                inventario[nombre] += cantidad
                print(f"  ✓ Se sumaron {cantidad} a '{nombre}'. Total: {inventario[nombre]}")
            else:
                inventario[nombre] = cantidad
                print(f"  ✓ Producto '{nombre}' agregado con {cantidad} unidades")
            contador += 1
        else:
            print(f"  ✗ No se agregó '{nombre}': {mensaje}")
    
    print(f"\n▶ Se agregaron {contador} productos al inventario")
    return inventario

# ---------- MÓDULO 4: ESTRUCTURA REPETITIVA (for) ----------
def mostrar_inventario(inventario):
    """
    Muestra todo el inventario usando un bucle for
    """
    print("\n" + "=" * 50)
    print("   INVENTARIO ACTUAL")
    print("=" * 50)
    
    # Bucle for para recorrer el diccionario
    if len(inventario) == 0:
        print("  El inventario está vacío")
    else:
        for producto, cantidad in inventario.items():
            print(f"  • {producto}: {cantidad} unidades")
    
    print("=" * 50)

# ---------- MÓDULO 5: PROGRAMA PRINCIPAL ----------
def main():
    """Función principal que coordina todos los módulos"""
    mostrar_bienvenida()
    
    # Llamar al módulo de bucle while
    inventario = agregar_multiple_productos()
    
    # Llamar al módulo de bucle for
    mostrar_inventario(inventario)
    
    print("\n¡Programa finalizado!")

# Punto de entrada
#if __name__ == "__main__":
 #   main()
# ============================================
# NUEVOS MÓDULOS PARA MENÚ INTERACTIVO
# ============================================

# ---------- MÓDULO DE MENÚ (condicional múltiple) ----------
def mostrar_menu():
    """Muestra las opciones del menú"""
    print("\n" + "-" * 40)
    print("   MENÚ PRINCIPAL")
    print("-" * 40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Salir")
    print("-" * 40)

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario"""
    if nombre in inventario:
        del inventario[nombre]
        return True, f"Producto '{nombre}' eliminado"
    else:
        return False, f"Producto '{nombre}' no encontrado"

def menu_principal():
    """
    Controla el flujo del programa usando condicional múltiple (if-elif-else)
    """
    inventario = {}  # Comenzar con inventario vacío
    mostrar_bienvenida()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        
        # ESTRUCTURA CONDICIONAL MÚLTIPLE
        if opcion == "1":
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre: ").lower()
            cantidad = int(input("Cantidad: "))
            
            es_valida, mensaje = validar_cantidad(cantidad)
            
            if es_valida:
                if nombre in inventario:
                    inventario[nombre] += cantidad
                    print(f"✓ Se sumaron {cantidad} a '{nombre}'. Total: {inventario[nombre]}")
                else:
                    inventario[nombre] = cantidad
                    print(f"✓ Producto '{nombre}' agregado con {cantidad} unidades")
            else:
                print(f"✗ {mensaje}")
        
        elif opcion == "2":
            mostrar_inventario(inventario)
        
        elif opcion == "3":
            print("\n--- ELIMINAR PRODUCTO ---")
            nombre = input("Nombre del producto a eliminar: ").lower()
            exito, mensaje = eliminar_producto(inventario, nombre)
            print(f"{'✓' if exito else '✗'} {mensaje}")
        
        elif opcion == "4":
            print("\n▶ ¡Hasta luego! Gracias por usar el sistema")
            break
        
        else:
            print("✗ Opción no válida. Elige 1, 2, 3 o 4")

# ---------- PROGRAMA PRINCIPAL (nueva versión) ----------
def main_v3():
    """Versión 3 del programa: con menú interactivo"""
    menu_principal()

# Cambia el punto de entrada:
if __name__ == "__main__":
    # main()      # Versión anterior (agregar múltiple)
    main_v3()      # Nueva versión (menú interactivo)
