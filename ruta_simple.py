import networkx as nx
import matplotlib.pyplot as plt

def ruta_simple(G, pos, origen, destino):
    """Calcula y dibuja la ruta más corta usando Dijkstra."""
    try:
        camino = nx.shortest_path(G, source=origen, target=destino, weight='weight')
        peso_total = nx.shortest_path_length(G, source=origen, target=destino, weight='weight')
    except nx.NetworkXNoPath:
        print(f"\nNo existe una ruta disponible entre {origen} y {destino}.")
        return

    print(f"\nRuta más eficiente desde el punto {origen} hasta {destino}:")
    print(camino)
    print(f"Peso total: {peso_total}\n")

    # Dibujar el grafo completo
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, node_size=300, node_color="lightgray", edge_color="gray",
            with_labels=True, font_size=7)

    # Aristas del camino
    aristas = list(zip(camino[:-1], camino[1:]))

    # Dibujar ruta
    nx.draw_networkx_nodes(G, pos, nodelist=camino, node_color="blue", node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color="blue", width=3)

    # Etiquetas de pesos
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

    plt.title(f"Ruta más corta de {origen} a {destino} (Peso total: {peso_total})")
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.001)