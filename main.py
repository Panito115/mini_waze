import networkx as nx
from grafo import G, pos, dibujar_grafo_actual
from ruta_simple import ruta_simple
from ruta_con_parada import ruta_con_parada
from ruta_obstaculo import ruta_con_obstaculo
from trafico import activar_trafico, restaurar_pesos, guardar_pesos_originales


def mostrar_menu():
    print("\n" + "="*40)
    print("        MINI WAZE — MENU PRINCIPAL")
    print("="*40)
    print("1. Ruta simple")
    print("2. Ruta con parada")
    print("3. Ruta con obstáculo")
    print("4. Activar tráfico")
    print("5. Desactivar tráfico (restaurar pesos)")
    print("6. Mostrar grafo actual")
    print("7. Salir")
    print("="*40)


def main():
    pesos_originales = guardar_pesos_originales(G)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            origen = int(input("Origen: "))
            destino = int(input("Destino: "))
            ruta_simple(G, pos, origen, destino)

        elif opcion == "2":
            origen = int(input("Origen: "))
            parada = int(input("Parada: "))
            destino = int(input("Destino: "))
            ruta_con_parada(G, pos, origen, parada, destino)

        elif opcion == "3":
            origen = int(input("Origen: "))
            obst = int(input("Obstáculo: "))
            destino = int(input("Destino: "))
            ruta_con_obstaculo(G, pos, origen, obst, destino)

        elif opcion == "4":
            activar_trafico(G)
            print("\n Tráfico activado.\n")

        elif opcion == "5":
            restaurar_pesos(G, pesos_originales)
            print("\nTráfico desactivado. Pesos restaurados.\n")

        elif opcion == "6":
            dibujar_grafo_actual()

        elif opcion == "7":
            print("\nGracias por usar Mini-Waze \n")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()