# Mini-Waze — Sistema de navegación con grafos

Este proyecto implementa una versión simplificada de **Waze**, utilizando un **grafo dirigido con pesos** para representar la Zona 1 de la Ciudad de Guatemala.  
El sistema permite calcular rutas óptimas, simular tráfico y visualizar dinámicamente los caminos.

---

## Área seleccionada
Se escogió la **Zona 1**, desde:

- 4a a 10a calle  
- 3a a 9a avenida  

Esta área se tradujo manualmente a un grafo dirigido, respetando:

- sentido de calles  
- intersecciones reales  
- conexiones principales  
- distancias aproximadas  

El mapa final contiene:

### 61 nodos  
### +80 aristas dirigidas  
### 10 puntos de interés (POI)

![Grafo inicial](imagenes/grafo%20algoritmia.JPG)

---

# Puntos de interés (POI)

El grafo incluye 10 nodos especiales destacados con colores:

| Color | Ubicación |
|-------|-----------|
| Amarillo | Casa Presidencial |
| Verde | Palacio Nacional |
| Rojo | Congreso |
| Azul | Mercado Central |
| Morado | Restaurante Long Wah |
| Café | Plaza Vivar |
| Rosado | Panadería Berna |
| Celeste | Plaza de la Constitución |
| Verde claro | Bar de Vic |
| Gris | Almacenes Cisne |

Estos colores permiten identificar POIs fácilmente en el grafo.

![Grafo con POIs](imagenes/grafo_marcado_algoritmia.png)

---

# Estructura del grafo

- Los nodos representan **intersecciones reales**.  
- Las aristas representan **calles dirigidas**.  
- Los pesos representan **costo/tiempo sin tráfico**, valores entre **1 y 5**.  

Ejemplo:

- 3 -> 2 peso=3
- 4 -> 3 peso=5
- 5 -> 4 peso=1

Los pesos se usan para calcular rutas óptimas mediante el algoritmo de Dijkstra.

---

# Simulación de tráfico 

El sistema permite simular “hora pico”.

Cuando se activa el tráfico:

- Pesos **4–5** -> se multiplican ×3  
- Pesos **2–3** -> se multiplican ×2  
- Pesos **1** -> permanecen igual  

Esto genera:

- rutas diferentes  
- costos totales más altos  
- congestión realista en vías principales  

![Grafo con tráfico](imagenes/grafo_completo.png)

---

# Funcionalidades del sistema

## 1. Ruta simple  
Calcula la ruta más corta entre dos puntos usando **Dijkstra** (NetworkX).

## 2. Ruta con parada  
Obliga a pasar por un punto intermedio antes de llegar al destino.

## 3. Ruta con obstáculo  
Bloquea un nodo y sus vecinos inmediatos.  
Simula:

- accidentes  
- protestas  
- calles cerradas  

## 4. Ruta con tráfico  
Actualiza dinámicamente los pesos y recalcula rutas considerando congestión.

## 5. Restaurar tráfico  
Regresa el grafo a sus pesos originales.

## 6. Visualizar grafo  
Dibuja el grafo en su estado actual (con o sin tráfico).

---

# Conclusión

Este proyecto implementa:

- Un grafo realista de la Zona 1  
- Tres algoritmos de navegación  
- Simulación de tráfico  
- Visualización dinámica en tiempo real  
- Diseño reproducible, limpio y documentado  
- Uso correcto de NetworkX, matplotlib y Dijkstra  

---