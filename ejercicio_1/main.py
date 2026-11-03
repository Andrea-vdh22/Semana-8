"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    return {(fila, columna): puestos[fila][columna] for fila in range(len(puestos)) for columna in range(len(puestos[fila]))}


def obtener_disponibles(puestos):
    return {(fila, columna) for fila in range(len(puestos)) for columna in range(len(puestos[fila])) if puestos[fila][columna] == 0}

if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)

    print("Mapa completo:")
    print("Puestos disponibles:", disponibles)
    print("Estado de (1, 2) mapa:", mapa.get((1, 2)))

    # TODO: agrega al menos un caso propio.
puestos_propios = [[0, 1], [1, 0], [0, 0]]
mapa_propios = crear_mapa(puestos_propios)
disponibles_propios = obtener_disponibles(puestos_propios)
print("Mapa propio:" , mapa_propios)
print("Puestos disponibles (propio):", disponibles_propios)

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.

