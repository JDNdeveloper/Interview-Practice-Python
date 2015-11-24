# Author: Jayden Navarro
# Date: 10/14/2015

import math

class Heap:
   class Node:
      def __init__(self, data=None, key=None):
         _data = data
         _key = key

   def __init__(self):
      self._heap = []
      self._size = 0
      self._isHeap = True

   def _boundsCheck(func):
      def wrapper(self, *args):
         if self._size == 0:
            return False
         elif len(args) > 0:
            pos = args[0]
            if pos < 0 or pos >= self._size:
               return False
         return func(self, *args)
      return wrapper

   def _confirmIsHeap(func):
      def wrapper(self, *args):
         if self._isHeap == False:
            self._buildHeap()
         return func(self, *args)
      return wrapper

   @property
   def size(self):
      return self._size

   @property
   def isHeap(self):
      return self._isHeap

   def insert(self, data, key):
      self._heap.append(self.Node(data=data, key=key))
      self._size += 1

   @_boundsCheck
   @_confirmIsHeap
   def extractMax(self):
      pass
      self._size -= 1

   @_boundsCheck
   @_confirmIsHeap
   def increaseKey(self, pos, key):
      return True

   @_boundsCheck
   @_confirmIsHeap
   def heapSort(self):
      pass
      _isHeap = False

   def buildHeap(self):
      _isHeap = True

   @_boundsCheck
   @_confirmIsHeap
   def _heapify(self, pos):
      pass
      
   @_boundsCheck
   def _parent(self, pos):
      return int(pos / 2 - 1) if pos % 2 == 0 else int(pos / 2)

   @_boundsCheck
   def _left(self, pos):
      return pos * 2 + 1

   @_boundsCheck
   def _right(self, pos):
      return pos * 2 + 2

if __name__ == "__main__":
   def decoratorTest():
      heap = Heap()
      assert heap.increaseKey(3, 2) == False
      assert heap.increaseKey(0, 3) == False
      heap.insert(2, 10)
      heap.insert(3, 13)
      heap.insert(2, 2)
      heap.insert(10, 4)
      assert heap.increaseKey(3, 10) == True
      assert heap.increaseKey(0, 3) == True
      assert heap.increaseKey(-1, 32) == False
      assert heap.increaseKey(4, 10) == False

   def parentTest():
      heap = Heap()
      heap._size = 11
      assert heap._parent(3) == 1
      assert heap._parent(4) == 1
      assert heap._parent(9) == 4
      assert heap._parent(10) == 4
      assert heap._left(5) == 11
      assert heap._left(7) == 15
      assert heap._left(8) == 17
      assert heap._right(4) == 10
      assert heap._right(6) == 14
      assert heap._right(2) == 6

   def heapTest():
      heap = Heap()
      assert heap.size == 0
      assert heap.isHeap == True
      for data in range(20):
         key = int(data / 2 + 5)
         heap.insert(data, key)
      assert heap.size == 20
      assert heap.isHeap == True
      assert 19 == heap.extractMax()
      assert 18 == heap.extractMax()
      assert heap.size == 18
      sortedList = list(self._heap)
      sortedList.sort()
      heap.heapSort()
      assert self._heap == sortedList
      assert heap.isHeap == False
      assert heap[0] == 0
      heap._heapify()
      assert heap[0] == 17
      assert heap.isHeap == True
      heap.heapSort()
      assert heap.isHeap == False
      assert heap.extractMax == 17
      assert heap.isHeap == True

   decoratorTest()
   parentTest()
   #heapTest()
