import heapq
from graph import Graph

def min_key(self, keys: list[int], visited: set[int]) -> int:
  """Finds the minimum key vertex from the set of vertices not yet included in MST.

  Args:
    keys (List[int]): The keys associated with vertices.
    visited (Set[int]): The set of visited vertices.

  Returns:
    int: The minimum key vertex.
  """
  min_key_vertex = -1
  min_key = float('inf')

  for vertex in range(self.num_vertices):
    if keys[vertex] < min_key and vertex not in visited:
      min_key_vertex = vertex
      min_key = keys[vertex]
  return min_key_vertex

def primMST(graph:Graph) -> Graph:
  """Constructs and returns the minimum spanning tree (MST) using Prim's algorithm.
  
  Args:
    graph (Graph): The input graph.
  Returns:
    Graph: Minimum Spanning Tree.
  """
  num_vertices = graph.num_vertices
  mst = Graph(num_vertices)
    
  visited = set()
    
  min_keys = [float('inf')] * num_vertices
  parent = [-1] * num_vertices

  min_keys[0] = 0
  parent[0] = -1
    
  for _ in range(num_vertices):
    vertex = graph.min_key(min_keys, visited)
    visited.add(vertex)
    if vertex != 0:
      weight = graph.graph[parent[vertex]][vertex]
      mst.addEdge(parent[vertex], vertex, weight)
      for neighbour in range(num_vertices):
        neigh_weight = graph.graph[vertex][neighbour]
        if neighbour not in visited and neigh_weight!= 0 and neigh_weight < min_keys[neighbour]:
          min_keys[neighbour] = neigh_weight
          parent[neighbour] = vertex
  return mst 

def primsMSTMinHeap(graph:Graph):
    """Constructs and returns the minimum spanning tree (MST) using Prim's algorithm.
    
    Args:
        graph (Graph): The input graph.

    Returns:
        Graph: Minimum Spanning Tree.
    """
    num_vertices = graph.n_vertices
    mst = Graph(num_vertices)
    
    visited = set()
    
    min_keys = [float('inf')] * num_vertices
    min_heap = [(0, 0)]
    parent = [-1] * num_vertices

    parent[0] = -1
    edgeCount = 0
    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        if parent[vertex]!= -1: # Starting Vertex
            mst.addEdge(parent[vertex],vertex,weight)
            edgeCount += 1
            if edgeCount == num_vertices - 1:
                break
            
        for neighbour in range(num_vertices):
            neigh_weight = graph.graph[vertex][neighbour]
            if neighbour not in visited and neigh_weight!= 0 and neigh_weight < min_keys[neighbour]:
                min_keys[neighbour] = neigh_weight
                parent[neighbour] = vertex
                heapq.heappush(min_heap,(neigh_weight,neighbour))
                
    return mst

