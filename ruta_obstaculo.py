import networkx as nx
import matplotlib.pyplot as plt
from grafo import G, pos


def ruta_con_obstaculo(G, origen, obstaculo, destino):
    """Calcula la ruta evitando el nodo obstáculo y sus vecinos inmediatos. """
    # alrededores inmediatos del nodo obstáculo
    vecinos = list(G.neighbors(obstaculo)) + [n for n in G.predecessors(obstaculo)]
    nodos_bloqueados = set(vecinos + [obstaculo])

    # crear copia del grafo sin los nodos bloqueados
    G2 = G.copy()
    G2.remove_nodes_from(nodos_bloqueados)

    # verificar si hay ruta
    if not nx.has_path(G2, origen, destino):
        print(f"No hay rutas disponibles evitando el punto {obstaculo} y sus alrededores indmediatos.")
        return None

    ruta = nx.shortest_path(G2, source=origen, target=destino, weight='weight')
    peso = nx.shortest_path_length(G2, source=origen, target=destino, weight='weight')

    return ruta, peso, nodos_bloqueados


if __name__ == "__main__":
    origen = 12
    destino = 40
    obstaculo = 16  

    resultado = ruta_con_obstaculo(G, origen, obstaculo, destino)
    if resultado is None:
        raise SystemExit("Error, no se pudo calcular la ruta.")

    ruta, peso, bloqueados = resultado

    print(f"Ruta evitando nodo {obstaculo}: {ruta}")
    print(f"Peso total: {peso}")
    print(f"Nodos bloqueados: {bloqueados}")

    # dibujar el grafo base
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, node_size=300, node_color='lightgray', edge_color='gray', with_labels=True, font_size=7, arrows=True, arrowstyle='-|>', arrowsize=15)

    # resaltar nodos bloqueados
    nx.draw_networkx_nodes(G, pos, nodelist=bloqueados, node_color='black', node_size=500)

    # resaltar ruta
    nx.draw_networkx_nodes(G, pos, nodelist=ruta, node_color='blue', node_size=400)

    aristas = list(zip(ruta[:-1], ruta[1:])) # aristas de la ruta
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color='blue', width=3, arrows=True, arrowstyle='-|>', arrowsize=20)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    plt.title(f"Ruta evitando nodo {obstaculo}, peso total de la ruta: {peso})")
    plt.axis('off')
    plt.tight_layout()
    plt.show()


