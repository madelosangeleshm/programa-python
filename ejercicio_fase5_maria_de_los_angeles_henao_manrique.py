"""Código para calcular precios finales de productos en un menú."""

# Actividad: Fase 5 - Evaluación final POA
# Estudiante: María de los Ángeles Henao Manrique
# Grupo: 213022_500
# Programa: Ingeniería Multimedia
# Código fuente: Autoría propia

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """Calcula el precio final aplicando un 15% de descuento si cumple las reglas de negocio."""

    if categoria_producto == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return int(precio_base - descuento)
    else:
        return int(precio_base)

def main():
    """Imprime el reporte de precios finales del menú."""
    # Matriz con nombre del producto, categoría y precio base
    menu = [
        ["Hamburguesa", "Plato principal", 35000],
        ["Perro caliente", "Plato principal", 24000],
        ["Gaseosa", "Bebida", 8000],
        ["Limonada", "Bebida", 10000],
        ["Helado de vainilla", "Postre", 6500],
        ["Torta de tres leches", "Postre", 9500]
    ]

    # Parámetros definidos para la promoción
    categoria_objetivo = "Bebida"
    umbral_precio = 6000

    print("\nReporte de precios finalesdel menú:\n")
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Precio final con o sin descuento según las reglas de negocio
        precio_final = calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral_precio)

        # Resultados finales del producto
        print(f"Producto: {nombre:<20} | Precio base: ${precio_base:>7,} | Precio final: ${precio_final:>7,}")

if __name__ == "__main__":
    main()
