# Author: Jayden Navarro
# Date: 10/14/2015

import sys
from collections import Counter
from heapq import heappush, heappop, heapify
from GraphADT import Graph

def BFS(graph, root):
   distance = {}
   parent = {}
   for node in graph.nodes:
      distance[node] = sys.maxsize
      parent[node] = None
   queue = []
   distance[root] = 0
   queue.append(root)
   while len(queue) > 0:
      node = queue.pop(0)
      for adjArc in graph.adjList(node):
         adjNode = adjArc.dest
         if distance[adjNode] == sys.maxsize:
            distance[adjNode] = distance[node] + 1
            parent[adjNode] = node
            queue.append(adjNode)
   return distance, parent

def DFS(graph, root):
   distance = {}
   parent = {}
   for node in graph.nodes:
      distance[node] = sys.maxsize
      parent[node] = None
   stack = []
   distance[root] = 0
   stack.append(root)
   while len(stack) > 0:
      node = stack.pop()
      for adjArc in graph.adjList(node):
         adjNode = adjArc.dest
         if distance[adjNode] == sys.maxsize:
            distance[adjNode] = distance[node] + 1
            parent[adjNode] = node
            stack.append(adjNode)
   return distance, parent

class NodePlus:
   def __init__(self, node, distance=sys.maxsize, parent=None):
      self.node = node
      self.distance = distance
      self.parent = parent
   def __eq__(self, other):
      return self.node == other.node
   def __lt__(self, other):
      return self.distance < other.distance
   def __gt__(self, other):
      return self.distance > other.distance
   def __repr__(self):
      return str(self.node)
   def __hash__(self):
      return hash(self.node)

def Dijkstras(graph, root):
   heap = []
   for node in graph.nodes:
      node.distance = 0
      node.distance = sys.maxsize
      node.parent = None
      heappush(heap, node)
   root.distance = 0
   while len(heap) > 0:
      heapify(heap)
      node = heappop(heap)
      for adjArc in graph.adjList(node):
         adjNode = adjArc.dest
         adjWeight = adjArc.weight
         if node.distance + adjWeight < adjNode.distance:
            adjNode.distance = node.distance + adjWeight
            adjNode.parent = node

if __name__ == "__main__":
   graph = Graph()
   graph.addArc('A', 'B')
   graph.addArc('A', 'C')
   graph.addArc('B', 'E')
   graph.addArc('E', 'F')
   graph.addArc('C', 'G')
   graph.addArc('G', 'D')
   print("Graph 1:")
   print(graph)

   distance, parent = BFS(graph, 'A')
   assert distance == {'G': 2, 'B': 1, 'E': 2, 'F': 3, 'A': 0, 'C': 1, 'D': 3}
   assert parent == {'G': 'C', 'B': 'A', 'E': 'B', 'F': 'E', \
      'A': None, 'C': 'A', 'D': 'G'}
   print("BFS:")
   print("Distances: %s" % str(distance))
   print("Parents: %s" % str(parent))
   print()

   graph.addArc('A', 'D')
   distance, parent = DFS(graph, 'A')
   assert distance == {'G': 2, 'B': 1, 'E': 2, 'F': 3, 'A': 0, 'C': 1, 'D': 1}
   assert parent == {'G': 'C', 'B': 'A', 'E': 'B', 'F': 'E', \
      'A': None, 'C': 'A', 'D': 'A'}
   print("DFS:")
   print("Distances: %s" % str(distance))
   print("Parents: %s" % str(parent))
   print()

   graph2 = Graph()
   a = NodePlus('A')
   b = NodePlus('B')
   c = NodePlus('C')
   d = NodePlus('D')
   e = NodePlus('E')
   f = NodePlus('F')
   g = NodePlus('G')
   graph2.addArc(a, b, 22)
   graph2.addArc(a, c, 11)
   graph2.addArc(b, e, 10)
   graph2.addArc(e, f, 5)
   graph2.addArc(c, g, 100)
   graph2.addArc(c, b, 5)
   graph2.addArc(g, d, 2)
   print("Graph 2:")
   print(graph2)

   def printNodePlusGraph(graph):
      for node in graph.nodes:
         print("Node: %s, Distance: %d, Parent: %s" 
            % (node.node, node.distance, node.parent))
      print()

   def checkNodePlusGraph(graph, checkTuples):
      graphTuples = []
      for node in graph.nodes:
         graphTuples.append((node.node, node.distance, node.parent))
      assert Counter(checkTuples) == Counter(graphTuples)

   Dijkstras(graph2, a)
   print("Dijkstras on Graph 2:")
   printNodePlusGraph(graph2)
   checkNodePlusGraph(graph2, [('E', 26, b), ('A', 0, None), ('B', 16, c), 
      ('D', 113, g), ('C', 11, a), ('G', 111, c), ('F', 31, e)])


   graph3 = Graph()
   graph3.addArc(a, b, 2)
   graph3.addArc(b, c, 2)
   graph3.addArc(c, d, 2)
   graph3.addArc(d, e, 2)
   graph3.addArc(e, f, 2)
   graph3.addArc(a, f, 50)
   graph3.addArc(f, g, 10)
   print("Graph 3:")
   print(graph3)

   Dijkstras(graph3, a)
   print("Dijkstras on Graph 3:")
   printNodePlusGraph(graph2)
   checkNodePlusGraph(graph2, [('B', 2, a), ('F', 10, e), ('G', 20, f), 
      ('D', 6, c), ('A', 0, None), ('C', 4, b), ('E', 8, d)])
