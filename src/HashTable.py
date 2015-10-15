# Author: Jayden Navarro
# Date: 10/14/2015

class HashTable():

   LOAD_THRESHOLD = 0.3

   GOLDEN_VALUE = 0.618034

   LOW_CAP = 10

   def __init__(self, capacity=-1):
      self.size = 0
      self.capacity = max(self.LOW_CAP, capacity)
      self.table = [None] * self.capacity

   def loadFactor(self):
      return self.size / self.capacity

   def resize(self):
      oldTable = self.table
      self.capacity *= 2
      self.table = [None] * self.capacity
      for bucket in oldTable:
         if bucket != None:
            for element in bucket:
               self._insert(element)

   def insert(self, element):
      self.size += 1
      if self.loadFactor() > self.LOAD_THRESHOLD:
         self.resize()
      self._insert(element)

   def _insert(self, element):
      hashNum = self._hash(element)
      if self.table[hashNum] == None:
         self.table[hashNum] = []
      self.table[hashNum].append(element)

   def find(self, element):
      bucket = self.table[self._hash(element)]
      if bucket != None:
         if element in bucket:
            return True
      return False

   def remove(self, element):
      self.size -= 1
      bucket = self.table[self._hash(element)]
      if bucket != None:
         if element in bucket:
            bucket.remove(element)

   def _hash(self, element):
      return int(self.capacity * (element * self.GOLDEN_VALUE - 
         int(element * self.GOLDEN_VALUE)))

HT = HashTable()

for i in range(32):
   HT.insert(i)

assert HT.find(23) == True
assert HT.find(32) == False
HT.remove(23)
assert HT.find(23) == False

print("Hash Table Capacity: %d" % HT.capacity)
print("Hash Table Entries: %d" % HT.size)
print("Hash Table Load Factor: %0.4f" % HT.loadFactor())
