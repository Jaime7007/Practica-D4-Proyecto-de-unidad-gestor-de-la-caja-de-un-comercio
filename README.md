# Aplicación de Caja Registradora (Consola en Python)

Aplicación de consola desarrollada en **Python** que simula el funcionamiento básico de un terminal punto de venta (TPV) o caja registradora diaria. Permite registrar operaciones con distintos métodos de pago, anular el último movimiento, consultar estadísticas acumuladas en tiempo real y emitir un resumen de cierre de jornada.

Hecho por: Aitor y JaimeMG

## Funcionalidades Principales

1. **Registrar una venta:**

   * Solicita el importe en euros (`€`), admitiendo tanto punto (`.`) como coma (`,`) como separador decimal.

   * Valida que el importe sea numérico y estrictamente mayor que `0`.

   * Despliega un submenú validado para seleccionar la forma de pago (**Efectivo**, **Tarjeta** o **Bizum**).

2. **Anular la última venta:**

   * Elimina la última operación registrada (comportamiento tipo pila / LIFO) y muestra el detalle de la venta cancelada.

   * Controla el estado de caja vacía para evitar errores de ejecución.

3. **Consultar estadísticas del día:**

   * Calcula y muestra por pantalla:

     * **Total recaudado (`€`)**

     * **Número total de operaciones**

     * **Importe medio por venta (`€`)**

     * **Venta mayor registrada (`€`)**

4. **Cerrar caja y salir:**

   * Genera el informe final de cierre de jornada con el resumen económico y finaliza de forma controlada el bucle principal.

## Requisitos Técnicos Implementados

* **Menú interactivo en bucle (`while`):** Mantiene la aplicación activa hasta que el usuario selecciona explícitamente la opción de cierre.

* **Selección múltiple (`if / elif / else`):** Gestión clara de las opciones del menú principal y del submenú de formas de pago.

* **Patrones clásicos de recorrido de listas (Capítulo 8):**

  * **Patrón Contador:** Conteo de operaciones válidas realizadas (`num_operaciones`).

  * **Patrón Acumulador:** Suma progresiva de los importes cobrados (`total_dia`).

  * **Patrón Máximo:** Búsqueda del importe más alto registrado durante la jornada (`venta_mayor`).

  * **Patrón Indicador / Bandera lógica (`boolean`):** Control de estados de validación y existencia de datos (`valido`, `registrado`, `hay_datos`, `salir`).

* **Modularidad y documentación:** Código dividido en funciones con responsabilidad única y documentadas mediante *docstrings* estándar (descripción, parámetros `Args` y valores de retorno `Returns`).

* **Control robusto de excepciones (`try / except ValueError`):** Todas las entradas por teclado (`input`) están protegidas frente a caracteres no numéricos o entradas vacías, evitando interrupciones inesperadas.

## Estructura del Código

| Función | Responsabilidad |
| ----- | ----- |
| `seleccionar_forma_pago()` | Muestra el submenú de métodos de pago y valida la elección entre `1` y `3`. |
| `registrar_venta(lista_ventas)` | Valida el importe positivo, invoca la selección de pago y añade `[importe, forma_pago]`. |
| `anular_ultima_venta(lista_ventas)` | Extrae y elimina el último registro mediante `.pop()` si existen ventas previas. |
| `calcular_estadisticas(lista_ventas)` | Recorre la lista aplicando los patrones de contador, acumulador, máximo y cálculo de media. |
| `consultar_estadisticas(lista_ventas)` | Formatea e imprime el informe de métricas parciales del día. |
| `cerrar_caja(lista_ventas)` | Muestra el balance final de cierre de caja o avisa si no hubo actividad. |
| `main()` | Orquesta la inicialización de datos y el bucle principal del menú. |

## Cómo Ejecutar el Proyecto

### Requisitos previos

* Tener instalado **Python 3.8 o superior** (no requiere librerías externas; utiliza únicamente la biblioteca estándar).

### Ejecución desde terminal

1. Guarda el código fuente en un archivo llamado `caja_registradora.py`.

2. Abre una terminal en la carpeta donde se encuentre el archivo.

3. Ejecuta el siguiente comando:

```bash
python caja_registradora.py
```

*(En sistemas Linux o macOS puede ser necesario usar `python3 caja_registradora.py`)*.

## Plan de Pruebas y Casos Frontera

| ID | Escenario / Caso frontera | Entrada del usuario | Resultado esperado |
| ----- | ----- | ----- | ----- |
| **CP-01** | Opción de menú fuera de rango inferior | `0` | Muestra error de opción incorrecta y repite el menú. |
| **CP-02** | Opción de menú fuera de rango superior | `5` | Muestra error de opción incorrecta y repite el menú. |
| **CP-03** | Entrada no numérica en menú principal | `"abc"` o `""` | Captura `ValueError`, informa del error y no rompe el bucle. |
| **CP-04** | Importe límite inferior inválido (cero) | `0` | Rechaza la venta por ser $\le 0$; no pide forma de pago. |
| **CP-05** | Importe negativo | `-15.50` | Rechaza la venta por ser menor que `0`. |
| **CP-06** | Importe decimal válido mínimo / normal | `0.01` o `25,5` $\rightarrow$ pago `2` | Registra `[0.01, "Tarjeta"]` o `[25.5, "Tarjeta"]` y confirma. |
| **CP-07** | Importe no numérico | `"cien"` | Captura `ValueError` y vuelve al menú sin registrar venta. |
| **CP-08** | Submenú de pago inválido y texto | `9`, luego `"bizum"`, luego `3` | Repite el submenú hasta recibir `3` y asigna `"Bizum"`. |
| **CP-09** | Anular venta con caja vacía | Opción `2` con `lista_ventas = []` | Muestra aviso de que no hay ventas para anular; la lista sigue vacía. |
| **CP-10** | Anular última venta tras varias ventas | Ventas `[10.0, "Efectivo"]`, `[30.0, "Bizum"]` $\rightarrow$ Opción `2` | Elimina solo la venta de `30.00 € (Bizum)` y conserva la de `10.00 €`. |
| **CP-11** | Consultar estadísticas con caja vacía | Opción `3` con `lista_ventas = []` | Muestra `"Aviso: La caja está vacía."` sin provocar división por cero. |
| **CP-12** | Estadísticas con una sola venta | Una venta de `40.0` $\rightarrow$ Opción `3` | Total `40.00 €`, operaciones `1`, media `40.00 €`, venta mayor `40.00 €`. |
| **CP-13** | Cerrar caja sin ventas previas | Opción `4` con `lista_ventas = []` | Muestra resumen indicando jornada sin ventas y finaliza el programa. |
| **CP-14** | Cerrar caja tras ventas y anulaciones | Tras registrar y anular $\rightarrow$ Opción `4` | Muestra el resumen exacto con los datos restantes y termina el bucle. |
