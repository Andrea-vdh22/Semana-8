"""EJERCICIO 10 — Lógica del reporte

Implementa generar_reporte(productos). Cada producto tiene nombre único,
precio y stock enteros no negativos, y categoria.
Devuelve un diccionario con:
- disponibles: lista de nombres con stock > 0, en el orden original.
  Usa filter y map con lambda.
- valor_total: suma de precio * stock de todos los productos.
  Usa map y reduce con lambda, con valor inicial 0.
- hay_agotados: booleano que indica si algún stock es 0.
  Usa any sobre map con lambda.
- categorias: set con todas las categorías. Usa comprensión de sets.
- precios_con_recargo: lista de tuplas (nombre, precio con recargo del 10 %),
  solo para productos con stock > 0, en el orden original.
  Define una lambda para el recargo, redondeado a dos decimales con round,
  e invócala dentro de una comprensión de listas.
No modifiques productos ni imprimas dentro de la función.
Para [] devuelve listas y set vacíos, valor_total=0 y hay_agotados=False.
"""

# TODO: importa reduce desde functools.


def generar_reporte(productos):
  if not productos:
    diccionario = {"disponibles": [], "valor_total": 0, "hay_agotados": False, "categorias": set(), "precios_con_recargo": []}
  diccionario = [map(lambda x: x["nombre"], filter(lambda x: x["stock"] > 0, productos))]
  valor_total = reduce(lambda contador, x: contador +x, (map(lambda x: x["precio"] * x["stock"], productos)), 0)
  hay_agotados = any(map(lambda x: x["stock"] == 0, productos))
  categorias = {x["categoria"] for x in productos}
  recargo = lambda precio: round(precio * 1.1, 2)
  precios_con_recargo = [(x["nombre"], recargo(x["precio"])) for x in productos if x["stock"] > 0]
  diccionario = {"disponibles": diccionario, "valor_total": valor_total, "hay_agotados": hay_agotados, "categorias": categorias, "precios_con_recargo": precios_con_recargo}
  return diccionario
        
