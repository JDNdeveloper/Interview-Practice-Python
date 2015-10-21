# Author: Jayden Navarro
# Date: 10/14/2015

import math

# Param: A list with integers steadily increasing by one, 
# but missing a single element in the sequence. 
#
# Return: The missing int.
def findMissingInt(array):
   if len(array) == 0:
      return None
   lowerMid = math.floor((len(array) - 1) / 2)
   upperMid = math.ceil((len(array) - 1) / 2)
   leftDiff = array[lowerMid] - array[0]
   rightDiff = array[-1] - array[upperMid]
   if leftDiff > rightDiff:
      return findMissingInt(array[0 : lowerMid + 1])
   elif rightDiff > leftDiff:
      return findMissingInt(array[upperMid : len(array)])
   else:
      return array[lowerMid] + 1

assert findMissingInt([3, 4, 5, 7, 8]) == 6
assert findMissingInt([9, 11, 12, 13, 14]) == 10
assert findMissingInt([232, 234, 235, 236]) == 233
assert findMissingInt([72, 73, 74, 75, 76, 78]) == 77
