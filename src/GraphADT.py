# Author: Jayden Navarro
# Date: 10/14/2015

from collections import Counter

class Arc:

   def __init__(self):
      self.dest = None
      self.weight = 1

   def __eq__(self, other):
      return self.dest == other.dest

   def __repr__(self):
      return str(self.weight) + "->" + str(self.dest)

   def __hash__(self):
      return hash(self.dest)

class Graph:
   def __init__(self):
      self._graph = {}

   @property
   def nodes(self):
      return list(self._graph.keys())

   @property
   def arcs(self):
      arcs = []
      for adjList in self._graph.values():
         for arc in adjList:
            arcs.append(arc)
      return arcs

   # adds arc, if arc exists, it updates the weight
   def addArc(self, n1, n2, weight=1):
      if not isinstance(weight, int) or weight < 1:
         return
      arc = Arc()
      arc.dest = n2
      arc.weight = weight
      if n1 in self._graph:
         if arc not in self._graph[n1]:
            self._graph[n1].append(arc)
         else:
            self.removeArc(n1, n2)
            self.addArc(n1, n2, weight)
      else:
         self._graph[n1] = [arc]
      if n2 not in self._graph:
         self._graph[n2] = []

   def removeArc(self, n1, n2):
      if n1 in self._graph:
         arc = Arc()
         arc.dest = n2
         if arc in self._graph[n1]:
            self._graph[n1].remove(arc)

   def isArc(self, n1, n2, weight=-1):
      arc = Arc()
      arc.dest = n2
      arc.weight = weight
      if n1 not in self._graph:
         return False
      elif weight == -1:
         return arc in self._graph[n1]
      else:
         return arc in self._graph[n1] and weight \
            == self._graph[n1][self._graph[n1].index(arc)].weight

   def getArc(self, n1, n2):
      tempArc = Arc()
      tempArc.dest = n2
      if n1 in self._graph:
         if tempArc in self._graph[n1]:
            return self._graph[n1][self._graph[n1].index(tempArc)]

   def adjList(self, n):
      if n in self._graph:
         return self._graph[n]

   def __str__(self):
      string = ""
      for node, adjList in self._graph.items():
         string += str(node) + ": "
         for arc in adjList:
            string += str(arc) + ", "
         if len(adjList) != 0:
            string = string[:-2]
         string += '\n'
      return string

def tests():
   graph = Graph()
   graph.addArc('A', 'B')
   graph.addArc('B', 'C')
   graph.addArc('B', 'A')
   assert Counter(graph.nodes) == Counter(['A', 'B', 'C'])
   assert graph.isArc('B', 'C') == True
   assert graph.isArc('C', 'B') == False
   graph.removeArc('B', 'C')
   assert graph.isArc('B', 'C') == False
   assert graph.getArc('A', 'B').weight == 1
   graph.addArc('A', 'B', weight=55)
   assert graph.getArc('A', 'B').weight == 55

   print(graph.adjList('B'))
   print(graph)

if __name__ == "__main__":
   tests()
