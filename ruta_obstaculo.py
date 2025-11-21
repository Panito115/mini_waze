import networkx as nx
import matplotlib.pyplot as plt

def ruta_con_obstaculo(G, pos, origen, obstaculo, destino):
    """Calcula una ruta evitando el nodo obstáculo y sus vecinos inmediatos."""

    vecinos = list(G.neighbors(obstaculo)) + list(G.predecessors(obstaculo))
    nodos_bloqueados = set(vecinos + [obstaculo])

    # Copia del grafo sin los nodos bloqueados
    G2 = G.copy()
    G2.remove_nodes_from(nodos_bloqueados)

    # Validar ruta
    try:
        ruta = nx.shortest_path(G2, source=origen, target=destino, weight='weight')
        peso = nx.shortest_path_length(G2, source=origen, target=destino, weight='weight')
    except nx.NetworkXNoPath:
        print(f"\nNo hay rutas disponibles evitando el punto {obstaculo} y sus alrededores.")
        return

    print(f"\nRuta evitando nodo {obstaculo}: {ruta}")
    print(f"Peso total: {peso}")
    print(f"Nodos bloqueados: {nodos_bloqueados}")

    # Dibujar grafo base
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, node_size=300, node_color='lightgray', edge_color='gray',
            with_labels=True, font_size=7, arrows=True, arrowstyle='-|>', arrowsize=15)

    # Bloqueados
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_bloqueados, node_color='black', node_size=500)

    # Ruta
    aristas = list(zip(ruta[:-1], ruta[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=ruta, node_color='blue', node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color='blue', width=3,
                           arrows=True, arrowstyle='-|>', arrowsize=20)

    # Pesos
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

    plt.title(f"Ruta evitando nodo {obstaculo} (Peso total: {peso})")
    plt.axis('off')
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.001)