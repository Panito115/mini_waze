import networkx as nx
import matplotlib.pyplot as plt
from grafo import G, pos


def ruta_con_parada(G, origen, parada, destino):
    """Calcula la ruta óptima entre origen, parada y destino usando pesos."""
    # comprobar conexión de cada ruta
    if not nx.has_path(G, origen, parada):
        print(f"No hay camino desde {origen} hasta la parada {parada}.")
        return None
    if not nx.has_path(G, parada, destino):
        print(f"No hay camino desde la parada {parada} hasta {destino}.")
        return None

    ruta1 = nx.shortest_path(G, source=origen, target=parada, weight='weight')
    peso1 = nx.shortest_path_length(G, source=origen, target=parada, weight='weight')

    ruta2 = nx.shortest_path(G, source=parada, target=destino, weight='weight')
    peso2 = nx.shortest_path_length(G, source=parada, target=destino, weight='weight')

    # une las rutas sin repetir la parada
    ruta_completa = ruta1 + ruta2[1:]
    peso_total = peso1 + peso2

    return ruta_completa, peso_total, ruta1, peso1, ruta2, peso2


if __name__ == "__main__":
    origen = 12
    destino = 47
    parada = 22  

    resultado = ruta_con_parada(G, origen, parada, destino)

    if resultado is None:
        raise SystemExit("No se pudo calcular la ruta con parada.")

    ruta_completa, peso_total, ruta1, peso1, ruta2, peso2 = resultado

    print(f"Ruta con parada elegida: {origen} -> {parada} -> {destino}")
    print("Ruta 1 (Antes de la parada):", ruta1, f"(peso={peso1})")
    print("Ruta 2 (Después de la parada):", ruta2, f"(peso={peso2})")
    print("Ruta completa:", ruta_completa)
    print(f"Peso total: {peso_total}")

    # Dibujar grafo base
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, node_size=300, node_color='lightgray', edge_color='gray', with_labels=True, font_size=7, arrows=True, arrowstyle='-|>', arrowsize=15)

    # aristas de cada tramo
    aristas_ruta1 = list(zip(ruta1[:-1], ruta1[1:]))
    aristas_ruta2 = list(zip(ruta2[:-1], ruta2[1:]))

    # Dibujar nodos de la ruta
    nx.draw_networkx_nodes(G, pos, nodelist=ruta_completa, node_color='lightblue', node_size=400)

    # Dibujar cada tramo con color distinto y ancho mayor
    nx.draw_networkx_edges(G, pos, edgelist=aristas_ruta1, edge_color='blue', width=3, arrows=True, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_edges(G, pos, edgelist=aristas_ruta2, edge_color='purple', width=3, arrows=True, arrowstyle='-|>', arrowsize=20)

    # resaltar la parada
    nx.draw_networkx_nodes(G, pos, nodelist=[parada], node_color='yellow', node_size=550)

    # Etiquetas de pesos 
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    plt.title(f"Ruta con parada: {origen} - {parada} - {destino} (peso total: {peso_total})")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    

    