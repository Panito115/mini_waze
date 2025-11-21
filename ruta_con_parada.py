import networkx as nx
import matplotlib.pyplot as plt

def ruta_con_parada(G, pos, origen, parada, destino):
    """Calcula y dibuja la ruta óptima pasando por una parada definida."""

    # Validar rutas
    if not nx.has_path(G, origen, parada):
        print(f"\nNo existe ruta entre {origen} y {parada}.")
        return

    if not nx.has_path(G, parada, destino):
        print(f"\nNo existe ruta entre {parada} y {destino}.")
        return

    ruta1 = nx.shortest_path(G, source=origen, target=parada, weight='weight')
    peso1 = nx.shortest_path_length(G, source=origen, target=parada, weight='weight')

    ruta2 = nx.shortest_path(G, source=parada, target=destino, weight='weight')
    peso2 = nx.shortest_path_length(G, source=parada, target=destino, weight='weight')

    ruta_completa = ruta1 + ruta2[1:]
    peso_total = peso1 + peso2

    print(f"\nRuta con parada: {origen} → {parada} → {destino}")
    print(f"Ruta total: {ruta_completa}")
    print(f"Peso total: {peso_total}")

    # Dibujar grafo base
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, node_size=300, node_color='lightgray', edge_color='gray',
            with_labels=True, font_size=7, arrows=True, arrowstyle='-|>', arrowsize=15)

    # Tramos
    aristas_1 = list(zip(ruta1[:-1], ruta1[1:]))
    aristas_2 = list(zip(ruta2[:-1], ruta2[1:]))

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, nodelist=ruta_completa, node_color='lightblue', node_size=400)

    # Tramos en colores distintos
    nx.draw_networkx_edges(G, pos, edgelist=aristas_1, edge_color='blue', width=3)
    nx.draw_networkx_edges(G, pos, edgelist=aristas_2, edge_color='purple', width=3)

    # Parada marcada
    nx.draw_networkx_nodes(G, pos, nodelist=[parada], node_color='yellow', node_size=550)

    # Pesos
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

    plt.title(f"Ruta con parada (Peso total: {peso_total})")
    plt.axis('off')
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.001)