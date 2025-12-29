from functools import reduce

# --------------------------
# Funciones puras de ingreso
# --------------------------

# Convierte texto de nombres a tupla inmutable
def ingresar_estudiantes():
    return tuple(
        map(lambda x: x.strip(),
            input("Ingrese los nombres de los estudiantes separados por comas:\n").split(","))
    )

# Convierte texto de notas a tupla inmutable
def ingresar_notas():
    return tuple(
        map(lambda x: int(x.strip()),
            input("Ingrese las notas finales separadas por comas (en el mismo orden):\n").split(","))
    )


# --------------------------
# Funciones puras académicas
# --------------------------

def crear_registros(estudiantes, notas):
    return tuple(zip(estudiantes, notas))

def es_aprobado(registro, minima=70):
    return registro[1] >= minima

def obtener_aprobados(registros, minima=70):
    return tuple(filter(lambda r: es_aprobado(r, minima), registros))

def obtener_reprobados(registros, minima=70):
    return tuple(filter(lambda r: not es_aprobado(r, minima), registros))

def calcular_promedio(registros):
    return 0 if not registros else reduce(lambda a, r: a + r[1], registros, 0) / len(registros)

def obtener_maximo(registros):
    return reduce(lambda a, b: a if a[1] >= b[1] else b, registros)

def obtener_minimo(registros):
    return reduce(lambda a, b: a if a[1] <= b[1] else b, registros)

def aplicar_analisis(registros, funcion):
    return funcion(registros)


# --------------------------
# Presentación funcional
# --------------------------

def formatear_registro(registro):
    return f"{registro[0]}: {registro[1]}"

def generar_reporte(registros):
    analisis = (
        ("Promedio del grupo", lambda r: round(calcular_promedio(r), 2)),
        ("Cantidad de estudiantes", lambda r: len(r)),
        ("Cantidad de aprobados", lambda r: len(obtener_aprobados(r))),
        ("Cantidad de reprobados", lambda r: len(obtener_reprobados(r))),
        ("Mejor estudiante", lambda r: obtener_maximo(r)[0]),
        ("Nota máxima", lambda r: obtener_maximo(r)[1]),
        ("Peor estudiante", lambda r: obtener_minimo(r)[0]),
        ("Nota mínima", lambda r: obtener_minimo(r)[1]),
    )

    lineas_analisis = tuple(
        map(lambda p: f"{p[0]}: {aplicar_analisis(registros, p[1])}", analisis)
    )

    lineas_detalle = tuple(map(formatear_registro, registros))

    return "\n".join((
        "=== REPORTE ACADÉMICO FUNCIONAL ===",
        "",
        ">> Análisis general:",
        *lineas_analisis,
        "",
        ">> Detalle (nombre: nota):",
        *lineas_detalle
    ))


# --------------------------
# Programa principal
# --------------------------

def main():
    estudiantes = ingresar_estudiantes()
    notas = ingresar_notas()
    registros = crear_registros(estudiantes, notas)
    print(generar_reporte(registros))


if __name__ == "__main__":
    main()
