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
