from graph import Graph
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random


def get_connected_graph(N):
  """
  Generates a connected, undirected, and weighted graph with N vertices and a random number of edges (up to 1.5 times N) using the provided Graph class.

  Args:
      N: Number of vertices in the graph (must be positive).

  Returns:
      A Graph object representing the generated connected graph.
  """
  if N <= 0:
    raise ValueError("Number of vertices must be positive.")

  # Create a Graph object
  graph = Graph(N)

  # Ensure all vertices are connected initially (might create cycles)
  for i in range(N):
    for j in range(i+1, N):
      graph.addEdge(i, j, random.randint(1, 10))  # Add an edge with random weight

  # Maximum allowed edges (1.5 times N)
  max_edges = int(1.5 * N)

  # Randomly add or remove edges until desired number is reached
  current_edges = N * (N - 1) // 2  # All possible edges initially
  while current_edges != max_edges:
    if current_edges > max_edges:
      # Remove edges until reaching the limit
      v1 = random.randint(0, N - 1)
      v2 = random.randint(0, N - 1)
      if graph.graph[v1][v2] != 0:
        graph.graph[v1][v2] = 0
        graph.graph[v2][v1] = 0  # Remove edge in both directions
        current_edges -= 1
    else:
      # Add edges until reaching the limit
      v1 = random.randint(0, N - 1)
      v2 = random.randint(0, N - 1)
      if v1 != v2 and graph.graph[v1][v2] == 0:
        graph.addEdge(v1, v2, random.randint(1, 10))
        current_edges += 1

  return graph


def drawWeightedGraph(g:Graph,pos= None):
    graph = nx.from_numpy_array(np.array(g.graph))
    weights = nx.get_edge_attributes(graph,'weight')
    if pos is None:
        pos = nx.spring_layout(graph)  # Use a different layout if needed (e.g., nx.circular_layout)
    nx.draw(graph, pos,with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=weights,font_size=12)
    plt.show()
    plt.close()
    return pos