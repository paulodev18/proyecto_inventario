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
def buscar_producto(inventario):
    """
    Repetitiva (while): permite buacar productos
    """
    print("\n--- MODO BUSCAR PRODUCTOS ---")
    print("Escribe 'fin' para terminar\n")

    while True:
        nombre = input("Nombre del producto a buscar: ").lower()

        if nombre == 'fin':
            break

        if validar_producto_existe(inventario, nombre):
            print(f"✓ Producto '{nombre}' encontrado")
        else:
            print(f"✗ Producto '{nombre}' no encontrado")

    return inventario

# ============================================
# NUEVO MÓDULO: MODIFICAR CANTIDAD
# ============================================

def modificar_cantidad(inventario):
    """
    Permite aumentar o disminuir la cantidad de un producto existente
    Combina: bucle while (repetitivo) + condicionales
    """
    print("\n--- MODO MODIFICAR CANTIDAD ---")
    print("Escribe 'fin' en el nombre para terminar\n")

    while True:
        nombre = input("Nombre del producto a modificar: ").lower()

        if nombre == 'fin':
            break

        # Condicional: verificar si existe
        if nombre not in inventario:
            print(f"✗ Producto '{nombre}' no encontrado")
            continue  # Vuelve al inicio del bucle

        # Si existe, mostrar cantidad actual
        print(f"✓ Producto '{nombre}' tiene {inventario[nombre]} unidades")

        # Preguntar qué hacer (condicional múltiple)
        print("   ¿Qué deseas hacer?")
        print("   a) Aumentar cantidad")
        print("   b) Disminuir cantidad")
        print("   c) Cancelar")
        sub_opcion = input("   Elige (a/b/c): ").lower()

        if sub_opcion == 'a':
            aumento = int(input("   ¿Cuánto aumentar? "))
            if aumento > 0:
                inventario[nombre] += aumento
                print(f"   ✓ Nueva cantidad: {inventario[nombre]} unidades")
            else:
                print("   ✗ El aumento debe ser positivo")

        elif sub_opcion == 'b':
            disminucion = int(input("   ¿Cuánto disminuir? "))
            if disminucion > 0 and disminucion <= inventario[nombre]:
                inventario[nombre] -= disminucion
                print(f"   ✓ Nueva cantidad: {inventario[nombre]} unidades")
                # Si queda en cero, preguntar si eliminar
                if inventario[nombre] == 0:
                    eliminar = input("   Cantidad llegó a 0. ¿Eliminar producto? (s/n): ").lower()
                    if eliminar == 's':
                        del inventario[nombre]
                        print(f"   ✓ Producto '{nombre}' eliminado")
            elif disminucion <= 0:
                print("   ✗ La disminución debe ser positiva")
            else:
                print(f"   ✗ No se puede disminuir {disminucion}. Solo tiene {inventario[nombre]}")

        elif sub_opcion == 'c':
            print("   ✓ Operación cancelada")

        else:
            print("   ✗ Opción no válida")

    return inventario

# ============================================
# NUEVOS MÓDULOS PARA MANEJO DE PRECIOS
# ============================================

def agregar_precio(precios):
    """
    Permite agregar precios a los productos
    Usa bucle while + condicionales
    """
    print("\n--- AGREGAR PRECIOS ---")
    print("Escribe 'fin' en el nombre para terminar\n")
    
    while True:
        nombre = input("Nombre del producto: ").lower()
        
        if nombre == 'fin':
            break
        
        try:
            precio = float(input(f"Precio de '{nombre}': $"))
            if precio > 0:
                precios[nombre] = precio
                print(f"✓ Precio de '{nombre}' registrado: ${precio:.2f}")
            else:
                print("✗ El precio debe ser mayor que cero")
        except ValueError:
            print("✗ Precio inválido. Usa números (ej: 1.50)")
    
    return precios

def calcular_valor_total(inventario, precios):
    """
    Calcula el valor total del inventario (cantidad * precio)
    Usa bucle for + condicionales
    """
    total = 0
    productos_sin_precio = []
    
    for producto, cantidad in inventario.items():
        if producto in precios:
            total += precios[producto] * cantidad
        else:
            productos_sin_precio.append(producto)
    
    # Mostrar reporte (estructura secuencial)
    print("\n" + "=" * 50)
    print("   VALOR TOTAL DEL INVENTARIO")
    print("=" * 50)
    print(f"   Total: ${total:.2f}")
    
    if productos_sin_precio:
        print(f"\n   ⚠️ Productos sin precio definido:")
        for p in productos_sin_precio:
            print(f"      - {p}")
    
    return total

def mostrar_precios(precios):
    """Muestra todos los precios registrados (bucle for)"""
    print("\n" + "=" * 50)
    print("   LISTA DE PRECIOS")
    print("=" * 50)
    
    if len(precios) == 0:
        print("   No hay precios registrados")
    else:
        for producto, precio in precios.items():
            print(f"   • {producto}: ${precio:.2f}")
    
    print("=" * 50)

# ============================================
# MÓDULOS PARA PERSISTENCIA (guardar/cargar)
# ============================================

import json  # Módulo para guardar datos en formato JSON

def guardar_inventario(inventario, precios, archivo="inventario.json"):
    """
    Guarda el inventario y precios en un archivo (estructura secuencial)
    """
    try:
        datos = {
            "inventario": inventario,
            "precios": precios
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"\n✓ Datos guardados en '{archivo}'")
        return True
    except Exception as e:
        print(f"\n✗ Error al guardar: {e}")
        return False

def cargar_inventario(archivo="inventario.json"):
    """
    Carga el inventario y precios desde un archivo (estructura secuencial)
    Retorna: (inventario, precios)
    """
    try:
        with open(archivo, 'r') as f:
            datos = json.load(f)
        inventario = datos.get("inventario", {})
        precios = datos.get("precios", {})
        print(f"\n✓ Datos cargados desde '{archivo}'")
        print(f"   {len(inventario)} productos en inventario")
        print(f"   {len(precios)} precios registrados")
        return inventario, precios
    except FileNotFoundError:
        print(f"\n⚠️ Archivo '{archivo}' no encontrado. Comenzando con datos vacíos.")
        return {}, {}
    except Exception as e:
        print(f"\n✗ Error al cargar: {e}")
        return {}, {}

# ============================================
# 4. MÓDULO DEL MENÚ (combina secuencial + condicional)
# ============================================
def mostrar_menu():
    print("\n" + "-" * 40)
    print("   MENÚ PRINCIPAL")
    print("-" * 40)
    print("1. Agregar productos")
    print("2. Mostrar inventario")
    print("3. Eliminar productos")
    print("4. Buscar producto")
    print("5. Modificar cantidad")
    print("6. Agregar precios")
    print("7. Mostrar precios")
    print("8. Calcular valor total")
    print("9. Guardar datos")      # NUEVO
    print("10. Cargar datos")      # NUEVO
    print("11. Salir")             # CAMBIA A 11
    print("-" * 40)

def ejecutar_menu():
    # Intentar cargar datos al iniciar
    inventario, precios = cargar_inventario()
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-11): ")

        if opcion == "1":
            inventario = agregar_productos_multiple(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            inventario = eliminar_producto_multiple(inventario)
        elif opcion == "4":
            inventario = buscar_producto(inventario)
        elif opcion == "5":
            inventario = modificar_cantidad(inventario)
        elif opcion == "6":
            precios = agregar_precio(precios)
        elif opcion == "7":
            mostrar_precios(precios)
        elif opcion == "8":
            calcular_valor_total(inventario, precios)
        elif opcion == "9":        # NUEVO
            guardar_inventario(inventario, precios)
        elif opcion == "10":       # NUEVO
            inventario, precios = cargar_inventario()
        elif opcion == "11":       # CAMBIA A 11
            # Preguntar si guardar antes de salir (condicional)
            guardar = input("¿Guardar datos antes de salir? (s/n): ").lower()
            if guardar == 's':
                guardar_inventario(inventario, precios)
            mostrar_despedida()
            break
        else:
            print("✗ Opción no válida")

# ============================================
# 5. PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal que inicia el programa"""
    ejecutar_menu()


# Punto de entrada
if __name__ == "__main__":
    main()
