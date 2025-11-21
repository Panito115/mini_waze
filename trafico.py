import networkx as nx

def guardar_pesos_originales(G):
    """Guarda los pesos originales de todas las aristas en un diccionario."""
    pesos = {}
    for u, v, data in G.edges(data=True):
        pesos[(u, v)] = data["weight"]
    return pesos


def activar_trafico(G):
    """
    Modifica los pesos del grafo para simular tráfico.
    Reglas:
    - Pesos 4–5 → se multiplican x3  (tráfico pesado)
    - Pesos 2–3 → se multiplican x2  (tráfico moderado)
    - Pesos 1   → se mantienen igual (calles internas)
    """
    for u, v, data in G.edges(data=True):
        w = data["weight"]

        if w >= 4:
            data["weight"] = w * 3 
        elif w >= 2:
            data["weight"] = w * 2
        else:
            data["weight"] = w  #el peso 1 se queda igual que antes


def restaurar_pesos(G, pesos_originales):
    """Restaura los pesos originales del grafo."""
    for (u, v), w in pesos_originales.items():
        if G.has_edge(u, v):
            G[u][v]["weight"] = w