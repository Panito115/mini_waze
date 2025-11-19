import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
# se agregan todos los nodos
nodos_1_61 = list(range(1, 62))

G.add_nodes_from(nodos_1_61)
# se agrega la dirección y el peso
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)
G.add_edge(1, 2, weight=1)
G.add_edge(59, 60, weight=1)

# lo crea tipo ciudad
pos = {}
cols = 10

for idx, node in enumerate(G.nodes()):
    x = idx % cols
    y = -(idx // cols)
    pos[node] = (x, y)

# aca comienza a dibujarlo
plt.figure(figsize=(14, 8))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    font_size=7,
    arrows=True,
    arrowstyle='-|>',
    arrowsize=15
)

# Etiquetas de pesos
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7
)

plt.axis("off")
plt.tight_layout()
plt.show()

print("Total nodos:", G.number_of_nodes())
print("Total aristas:", G.number_of_edges())
