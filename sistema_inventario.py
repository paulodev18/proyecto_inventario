# ============================================
# SISTEMA DE INVENTARIO - VERSIÓN 1
# Conceptos: Secuencial + Modularidad básica
# ============================================

def mostrar_bienvenida():
    """Módulo 1: Muestra un mensaje de bienvenida (estructura secuencial)"""
    print("=" * 40)
    print("   SISTEMA DE INVENTARIO - Versión 1")
    print("=" * 40)
    print("Bienvenido al sistema de gestión de inventario")
    print("Este programa te ayudará a administrar tus productos")
    print("=" * 40)

def mostrar_instrucciones():
    """Módulo 2: Muestra instrucciones básicas (estructura secuencial)"""
    print("\n--- INSTRUCCIONES ---")
    print("1. Escribe el nombre del producto")
    print("2. Escribe la cantidad")
    print("3. El sistema lo guardará automáticamente")
    print("----------------------\n")

def main():
    """Función principal que coordina los módulos"""
    mostrar_bienvenida()
    mostrar_instrucciones()
    print("Fin del programa de demostración")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
# ============================================
# NUEVO MÓDULO CON ESTRUCTURA CONDICIONAL
# ============================================

def validar_cantidad(cantidad):
    """
    Módulo que valida una cantidad usando estructura condicional
    Retorna:
        - True si la cantidad es válida (mayor que 0)
        - False si es inválida
        - Un mensaje explicativo
    """
    if cantidad > 0:
        return True, f"Cantidad {cantidad} es válida"
    elif cantidad == 0:
        return False, "Error: la cantidad no puede ser cero"
    else:
        return False, "Error: la cantidad no puede ser negativa"

def main_v2():
    """Versión 2: Incorpora validación condicional"""
    mostrar_bienvenida()
    
    # Entrada de datos (secuencial)
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    
    # Llamada al módulo condicional
    es_valida, mensaje = validar_cantidad(cantidad)
    
    # Estructura condicional para mostrar resultado
    if es_valida:
        print(f"✓ Producto '{nombre}' agregado correctamente")
        print(f"  {mensaje}")
    else:
        print(f"✗ No se pudo agregar '{nombre}'")
        print(f"  {mensaje}")
    
    print("\n--- FIN DEL PROGRAMA ---")

# Comenta la ejecución anterior y usa la nueva:
if __name__ == "__main__":
# main() 	# Version 1
  main_v2()	# Version 2
