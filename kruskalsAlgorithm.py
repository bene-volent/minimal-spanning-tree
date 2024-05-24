import heapq
from graph import Graph

class UnionFind:
    def __init__(self, size: int) -> None:
        """
        Initializes Union-Find with given size.

        Args:
            size (int): The size of Union-Find.

        Raises:
            ValueError: If size is less than 0.
        """
        if size < 0:
            raise ValueError("Size of Union-Find must be greater than 0")

        
        self.size_components = [0] * size
        self.roots = [-1] * size
        
        for i in range(size):
            self.roots[i] = i
            self.size_components[i] = 1
            
    def find(self, component: int) -> int:
        """
        Finds the root of the component.

        Args:
            component (int): The component to find.

        Returns:
            int: The root of the component.
        """
        root = component
        
        while root != self.roots[root]:
            root = self.roots[root]
            
        # Path Compression
        while component != root:
            next_component =  self.roots[component]
            self.roots[component] = root
            component = next_component
        
        return root
    
    def union(self, compP: int, compQ: int) -> None:
        """
        Unites two components.

        Args:
            compP (int): First component.
            compQ (int): Second component.
        """
        rootP = self.find(compP)
        rootQ = self.find(compQ)
        
        if rootP == rootQ:
            return;
        
        if self.size_components[rootP] < self.size_components[rootQ]:
            self.size_components[rootQ] += self.size_components[rootP]
            self.roots[rootP] = self.roots[rootQ]
            self.size_components[rootP] = 0
        else:
            self.size_components[rootP] += self.size_components[rootQ]
            self.roots[rootQ] = self.roots[rootP]
            self.size_components[rootQ] = 0
            
        
    

                    
def kruskalMST(graph: Graph) -> Graph:
    """
    Applies Kruskal's algorithm to find Minimum Spanning Tree.

    Args:
        graph (Graph): The input graph.

    Returns:
        Graph: Minimum Spanning Tree.
    """
    mst = Graph(graph.n_vertices)
    edges = graph.getEdges()
    
    # Sort the edges in non-decreasing order
    edges.sort(key=lambda edge: edge[2])
    uf = UnionFind(graph.n_vertices)
    edgeCount = 0
    for edge in edges:
        u,v,weight = edge
        
        root_u = uf.find(u)
        root_v = uf.find(v)
    
        if root_u != root_v: # Dont belong to same component i.e. Dont make a cycle
            mst.addEdge(u,v,weight)
            uf.union(u,v)
            edgeCount+=1
            
            # Early Termination
            if edgeCount == mst.n_vertices - 1:
                break
    
    return mst

def kruskalMSTMinHeap(graph: Graph) -> Graph:
    """
    Applies Kruskal's algorithm to find Minimum Spanning Tree.

    Args:
        graph (Graph): The input graph.

    Returns:
        Graph: Minimum Spanning Tree.
    """
    mst = Graph(graph.n_vertices)
    edges = graph.getEdges()
    
    # Put the edges in minheap
    min_heap = []
    for u,v,weight in edges:
        heapq.heappush(min_heap,(weight,(u,v)))
        
    uf = UnionFind(graph.n_vertices)
    edgeCount = 0
    while min_heap:
        weight, (u,v) = heapq.heappop(min_heap)
        
        root_u = uf.find(u)
        root_v = uf.find(v)
    
        if root_u != root_v: # Dont belong to same component i.e. Dont make a cycle
            mst.addEdge(u,v,weight)
            uf.union(u,v)
            edgeCount+=1
            
            # Early Termination
            if edgeCount == mst.n_vertices - 1:
                break
    
    return mst
