import networkx as nx
from grafo import G, pos
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
    print("6. Mostrar grafo base")
    print("7. Salir")
    print("="*40)


def main():
    # Guarda los pesos iniciales antes de activar tráfico
    pesos_originales = guardar_pesos_originales(G)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                origen = int(input("Ingrese nodo origen: "))
                destino = int(input("Ingrese nodo destino: "))
                ruta_simple(G, pos, origen, destino)
            except:
                print("Error: ingrese nodos válidos.")

        elif opcion == "2":
            try:
                origen = int(input("Ingrese nodo origen: "))
                parada = int(input("Ingrese nodo de parada: "))
                destino = int(input("Ingrese nodo destino: "))
                ruta_con_parada(G, origen, parada, destino)
            except:
                print("Error: ingrese nodos válidos.")

        elif opcion == "3":
            try:
                origen = int(input("Ingrese nodo origen: "))
                obstaculo = int(input("Ingrese nodo obstáculo: "))
                destino = int(input("Ingrese nodo destino: "))
                ruta_con_obstaculo(G, origen, obstaculo, destino)
            except:
                print("Error: ingrese nodos válidos.")

        elif opcion == "4":
            activar_trafico(G)
            print("\n Tráfico activado. Pesos del grafo modificados.\n")

        elif opcion == "5":
            restaurar_pesos(G, pesos_originales)
            print("\n Tráfico desactivado. Pesos originales recuperados.\n")

        elif opcion == "6":
            from grafo import dibujar_grafo_base, info_grafo
            info_grafo()
            dibujar_grafo_base()

        elif opcion == "7":
            print("\n¡Gracias por usar Mini-Waze!\n")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()