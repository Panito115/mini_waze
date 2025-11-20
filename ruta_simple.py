import networkx as nx
import matplotlib.pyplot as plt
from grafo import G, pos


origen = 40
final = 1

# Obtener la ruta simple usando Dijkstra
camino = nx.shortest_path(G, source=origen, target=final, weight='weight')
peso_total = nx.shortest_path_length(G, source=origen, target=final, weight='weight')

print(f"Ruta más corta desde {origen} hasta {final}:")
print(camino)
print(f"Peso total: {peso_total}\n")

# Dibujar el grafo completo en gris
plt.figure(figsize=(14, 8))
nx.draw(G, pos, node_size=300, node_color="lightgray", edge_color="gray", with_labels=True, font_size=7)

# aristas de la ruta
aristas_camino = list(zip(camino[:-1], camino[1:]))

# Dibujar la ruta
nx.draw_networkx_nodes(G, pos, nodelist=camino, node_color="blue", node_size=400)
nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color="blue", width=3)

# Etiquetas de pesos
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

plt.title(f"Ruta más corta de {origen} a {final} (Peso total: {peso_total})")
plt.axis('off')
plt.show()