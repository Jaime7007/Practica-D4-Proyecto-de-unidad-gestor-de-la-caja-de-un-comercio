"""}==========O=========={
 Cabecera
 Aplicación de consola: Caja registradora. 
 Autores: Aitor & JaimeMG 
 Fecha: 23/11/2026 
 }==========O=========={"""


def seleccionar_forma_pago() -> str:
    """Solicita y valida la forma de pago mediante un submenú.

    Returns:
        str: Forma de pago seleccionada ("Efectivo", "Tarjeta" o "Bizum").
    """
    formas = {
        1: "Efectivo",
        2: "Tarjeta",
        3: "Bizum",
    }
    forma_seleccionada = ""
    valido = False

    while not valido:
        print("\n--- FORMA DE PAGO ---")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Bizum")
        try:
            opcion_pago = int(input("Elige una opción (1-3): "))
            if opcion_pago in formas:
                forma_seleccionada = formas[opcion_pago]
                valido = True
            else:
                print("Error: Opción de pago no válida. Introduce 1, 2 o 3.")
        except ValueError:
            print("Error: Debes introducir un número entero (1-3).")

    return forma_seleccionada


def registrar_venta(lista_ventas: list) -> list:
    """Pide un importe positivo y la forma de pago, y añade la venta a la lista.

    Args:
        lista_ventas (list): Lista de ventas actuales [[importe, forma_pago], ...].

    Returns:
        list: Lista de ventas actualizada.
    """
    registrado = False

    try:
        entrada = input("Introduce el importe de la venta (€): ").strip().replace(",", ".")
        importe = float(entrada)

        if importe > 0:
            forma_pago = seleccionar_forma_pago()
            venta_actual = [round(importe, 2), forma_pago]
            lista_ventas.append(venta_actual)
            registrado = True
        else:
            print("Error: El importe debe ser mayor que 0.")
    except ValueError:
        print("Error: El importe debe ser un valor numérico válido.")

    if registrado:
        print("¡Venta registrada correctamente!")

    return lista_ventas


def anular_ultima_venta(lista_ventas: list) -> list:
    """Elimina y muestra la última venta registrada si la lista no está vacía.

    Args:
        lista_ventas (list): Lista de ventas actuales.

    Returns:
        list: Lista de ventas actualizada.
    """
    if len(lista_ventas) > 0:
        ultima_venta = lista_ventas.pop()
        print(
            f"Éxito: Se ha anulado la última venta de "
            f"{ultima_venta[0]:.2f} € ({ultima_venta[1]})."
        )
    else:
        print("Aviso: No hay ninguna venta registrada para anular.")

    return lista_ventas


def calcular_estadisticas(lista_ventas: list) -> tuple:
    """Calcula el total, número de operaciones, media y venta máxima.

    Aplica los patrones de recorrido: contador, acumulador y máximo.

    Args:
        lista_ventas (list): Lista de ventas registradas.

    Returns:
        tuple: (total_dia, num_operaciones, importe_medio, venta_mayor)
    """
    total_dia = 0.0        # Patrón acumulador
    num_operaciones = 0    # Patrón contador
    venta_mayor = 0.0      # Patrón máximo

    for venta in lista_ventas:
        importe = venta[0]
        num_operaciones += 1
        total_dia += importe
        if importe > venta_mayor:
            venta_mayor = importe

    importe_medio = total_dia / num_operaciones if num_operaciones > 0 else 0.0
    return total_dia, num_operaciones, importe_medio, venta_mayor


def consultar_estadisticas(lista_ventas: list) -> None:
    """Muestra por pantalla las estadísticas acumuladas del día.

    Args:
        lista_ventas (list): Lista de ventas registradas.
    """
    hay_datos = len(lista_ventas) > 0  # Patrón indicador / bandera lógico

    if hay_datos:
        total_dia, num_operaciones, importe_medio, venta_mayor = calcular_estadisticas(
            lista_ventas
        )
        print("\n==============================")
        print("    CONSULTAS DEL DÍA       ")
        print("==============================")
        print(f"• Total recaudado  : {total_dia:.2f} €")
        print(f"• Nº de operaciones: {num_operaciones}")
        print(f"• Importe medio    : {importe_medio:.2f} €")
        print(f"• Venta mayor      : {venta_mayor:.2f} €")
        print("==============================")
    else:
        print("Aviso: La caja está vacía.")


def cerrar_caja(lista_ventas: list) -> None:
    """Muestra el resumen final de la jornada y cierra la caja.

    Args:
        lista_ventas (list): Lista de ventas registradas.
    """
    print("\n==============================")
    print("      CIERRE DE CAJA - RESUMEN")
    print("==============================")

    if len(lista_ventas) > 0:
        total_dia, num_operaciones, importe_medio, venta_mayor = calcular_estadisticas(
            lista_ventas
        )
        print(f"• Total del día    : {total_dia:.2f} €")
        print(f"• Total operaciones: {num_operaciones}")
        print(f"• Importe medio    : {importe_medio:.2f} €")
        print(f"• Venta máxima     : {venta_mayor:.2f} €")
    else:
        print("• Jornada finalizada sin ventas registradas.")

    print("==============================")
    print("Caja cerrada correctamente. ¡Hasta mañana!")


def main() -> None:
    """Bucle principal de la aplicación de caja registradora."""
    lista_ventas = []
    salir = False

    while not salir:
        print("\n========================================")
        print("    APLICACIÓN DE CAJA REGISTRADORA     ")
        print("========================================")
        print("1. Registrar una venta")
        print("2. Anular la última venta")
        print("3. Consultar estadísticas del día")
        print("4. Cerrar caja y salir")
        print("========================================")

        try:
            opcion = int(input("Elige una opción (1-4): "))

            if opcion == 1:
                lista_ventas = registrar_venta(lista_ventas)
            elif opcion == 2:
                lista_ventas = anular_ultima_venta(lista_ventas)
            elif opcion == 3:
                consultar_estadisticas(lista_ventas)
            elif opcion == 4:
                cerrar_caja(lista_ventas)
                salir = True
            else:
                print("Error: Opción incorrecta. Introduce un número del 1 al 4.")
        except ValueError:
            print("Error: Debes introducir un número entero del 1 al 4.")


if __name__ == "__main__":
    main()
