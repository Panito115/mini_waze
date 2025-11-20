import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph() # funcion dentro de nx que hace el grafico dirigo

nodos_1_61 = list(range(1, 62))
G.add_nodes_from(nodos_1_61)

# se agrega la dirección de nodos y sus pesos
G.add_edge(2, 1, weight=1)
G.add_edge(3, 2, weight=3)
G.add_edge(4, 3, weight=5)
G.add_edge(5, 4, weight=1)
G.add_edge(6, 5, weight=1)
G.add_edge(7, 6, weight=1)
G.add_edge(8, 7, weight=1)
G.add_edge(9, 8, weight=3)
G.add_edge(10, 9, weight=2)
G.add_edge(11, 1, weight=1)
G.add_edge(12, 11, weight=1)
G.add_edge(14, 3, weight=1)
G.add_edge(4, 15, weight=4)
G.add_edge(6, 16, weight=5)
G.add_edge(17, 7, weight=2)
G.add_edge(9, 18, weight=1)
G.add_edge(19, 10, weight=2)
G.add_edge(12, 13, weight=2)
G.add_edge(13, 14, weight=2)
G.add_edge(14, 15, weight=3)
G.add_edge(15, 16, weight=2)
G.add_edge(16, 17, weight=1)
G.add_edge(17, 18, weight=1)
G.add_edge(18, 19, weight=3)
G.add_edge(20, 12, weight=5)
G.add_edge(59, 60, weight=1)
G.add_edge(2, 13, weight=1)
G.add_edge(13, 22, weight=1)
G.add_edge(23, 14, weight=2)
G.add_edge(15, 24, weight=1)
G.add_edge(26, 17, weight=3)
G.add_edge(18, 27, weight=2)
G.add_edge(28, 29, weight=2)
G.add_edge(29, 19, weight=1)
G.add_edge(22, 21, weight=1)
G.add_edge(21, 20, weight=1)
G.add_edge(23, 22, weight=3)
G.add_edge(24, 23, weight=2)
G.add_edge(25, 24, weight=1)
G.add_edge(26, 25, weight=2)
G.add_edge(27, 26, weight=1)
G.add_edge(28, 27, weight=3)
G.add_edge(35, 30, weight=3)
G.add_edge(30, 20, weight=2)
G.add_edge(31, 36, weight=1)
G.add_edge(22, 31, weight=1)
G.add_edge(32, 23, weight=3)
G.add_edge(24, 38, weight=2)
G.add_edge(39, 33, weight=2)
G.add_edge(33, 26, weight=1)
G.add_edge(27, 34, weight=3)
G.add_edge(34, 40, weight=1)
G.add_edge(41, 28, weight=3)
G.add_edge(30, 31, weight=1)
G.add_edge(36, 35, weight=1)
G.add_edge(31, 32, weight=2)
G.add_edge(37, 36, weight=1)
G.add_edge(38, 37, weight=3)
G.add_edge(39, 38, weight=1)
G.add_edge(40, 39, weight=4)
G.add_edge(41, 40, weight=2)
G.add_edge(42, 43, weight=1)
G.add_edge(43, 44, weight=3)
G.add_edge(44, 45, weight=2)
G.add_edge(45, 46, weight=5)
G.add_edge(46, 47, weight=2)
G.add_edge(47, 48, weight=3)
G.add_edge(42, 35, weight=1)
G.add_edge(36, 43, weight=2)
G.add_edge(49, 37, weight=1)
G.add_edge(38, 45, weight=4)
G.add_edge(46, 39, weight=1)
G.add_edge(40, 47, weight=1)
G.add_edge(48, 41, weight=1)
G.add_edge(49, 42, weight=2)
G.add_edge(54, 49, weight=1)
G.add_edge(43, 50, weight=1)
G.add_edge(50, 55, weight=3)
G.add_edge(56, 51, weight=2)
G.add_edge(51, 44, weight=1)
G.add_edge(45, 52, weight=2)
G.add_edge(52, 58, weight=1)
G.add_edge(59, 46, weight=4)
G.add_edge(47, 60, weight=1)
G.add_edge(61, 53, weight=1)
G.add_edge(53, 48, weight=1)
G.add_edge(49, 50, weight=2)
G.add_edge(50, 51, weight=2)
G.add_edge(55, 54, weight=5)
G.add_edge(56, 55, weight=2)
G.add_edge(57, 56, weight=4)
G.add_edge(58, 57, weight=1)
G.add_edge(59, 58, weight=3)
G.add_edge(60, 59, weight=2)
G.add_edge(61, 60, weight=2)

# se crea la ciudad visualmente
filas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],          
    [11],
    [12,13,14,15,16,17,18,19],
    [29],          
    [20,21,22,23,24,25,26,27,28],          
    [30,31,32,33,34],          
    [35,36,37,38,39,40,41],       
    [42,43,44,45,46,47,48],
    [49,50,51,52,53],
    [54,55,56,57,58,59,60,61],           
]

pos = {}
ancho_total = 10.0   # cantidad de nodos por anchos

for fila_idx, fila in enumerate(filas):
    y = -fila_idx            # cada fila un poquito más abajo
    n = len(fila)
    if n == 1:
        xs = [ancho_total / 2.0]
    else:
        xs = [i * (ancho_total / (n - 1)) for i in range(n)]

    for x, node in zip(xs, fila):
        pos[node] = (x, y)

# aca comienza a dibujar el grafo con matplot
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
