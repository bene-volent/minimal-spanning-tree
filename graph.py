class Graph:
    def __init__(self, n_vertices: int) -> None:
        """
        Initializes a graph with given number of vertices.

        Args:
            nVertices (int): Number of vertices in the graph.
        """
        self.n_vertices = n_vertices
        self.graph = [[0]*n_vertices for i in range(n_vertices)] 
        
    def addEdge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """
        Adds an edge between two vertices with given weight.

        Args:
            vertex1 (int): First vertex of the edge.
            vertex2 (int): Second vertex of the edge.
            weight (int): Weight of the edge.
        """
        if vertex1 < 0 or vertex1 >= self.n_vertices or vertex2 < 0 or vertex2 >= self.n_vertices :
            return;
        self.graph[vertex1][vertex2] = weight;
        self.graph[vertex2][vertex1] = weight;
    
    def getEdges(self) -> list:
        """
        Retrieves all edges in the graph.

        Returns:
            list: List of all edges in the graph.
        """
        edges = []
        
        for i in range(self.n_vertices):
            for j in range(i+1,self.n_vertices): # Edges only count once and no self edges:
                if self.graph[i][j] != 0:
                    edges.append((i,j,self.graph[i][j]))

        return edges                
    
    def print(self) -> None:
        """Prints the edges and their weights in the graph."""
        print("Edge \tWeight")
        for i in range(self.n_vertices):
            for j in range(i, self.n_vertices): 
                if self.graph[i][j] != 0:  
                    print(f"{i} - {j} :\t{self.graph[i][j]}")
                    