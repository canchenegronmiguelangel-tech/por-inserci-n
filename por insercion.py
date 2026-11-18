"""
Ejercicio 2: Ordenamiento por Inserción
Problema: Ordenar una lista de tareas pendientes por prioridad
(1 = más urgente, 5 = menos urgente), como cuando se ordenan
cartas en la mano: cada nueva tarea se inserta en su lugar correcto.
"""


def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Desplaza a la derecha los elementos con prioridad mayor (menos urgentes)
        while j >= 0 and lista[j][1] > actual[1]:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta la tarea en su posición correcta
        lista[j + 1] = actual
    return lista


if __name__ == "__main__":
    tareas = [
        ("Lavar la ropa", 4),
        ("Entregar proyecto de ADA1", 1),
        ("Hacer compras", 3),
        ("Estudiar para el examen", 2),
        ("Ver una serie", 5),
        ("Pagar la renta", 1),
    ]

    print("Tareas sin ordenar:")
    for tarea, prioridad in tareas:
        print(f"  [Prioridad {prioridad}] {tarea}")

    insercion(tareas)

    print("\nTareas ordenadas por prioridad:")
    for tarea, prioridad in tareas:
        print(f"  [Prioridad {prioridad}] {tarea}")