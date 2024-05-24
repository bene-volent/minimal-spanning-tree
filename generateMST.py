from kruskalsAlgorithm import kruskalMSTMinHeap
from primsAlgorithm import primsMSTMinHeap
import getGraph

for i in [7,9,12]:
  g = getGraph.get_connected_graph(i)
  pos = getGraph.drawWeightedGraph(g)
  mstP = primsMSTMinHeap(g)
  mstK = kruskalMSTMinHeap(g)
  getGraph.drawWeightedGraph(mstP,pos)
  getGraph.drawWeightedGraph(mstK,pos)
