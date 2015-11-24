# Author: Jayden Navarro
# Date: 10/14/2015

def quickSort(data):
   sortedData = list(data)
   _quickSort(sortedData, 0, len(data) - 1)
   return sortedData

def _quickSort(data, left, right):
   if (right - left) < 1:
      return
   partitionIndex = _partition(data, left, right)
   _quickSort(data, left, partitionIndex - 1)
   _quickSort(data, partitionIndex + 1, right)

def _partition(data, left, right):
   pivot = _medianOfThree(data, left, right)
   pivotValue = data[pivot]

   _swap(data, pivot, right)

   storeIndex = left
   for index in range(left, right):
      if data[index] < pivotValue:
         _swap(data, index, storeIndex)
         storeIndex += 1
   _swap(data, storeIndex, right)

   return storeIndex

def _medianOfThree(data, left, right):
   middle = int((left + right) / 2)
   if (data[left] < data[right] and data[left] > data[middle]) or \
      (data[left] > data[right] and data[left] < data[middle]):
      return left
   elif (data[right] < data[left] and data[right] > data[middle]) or \
        (data[right] > data[left] and data[right] < data[middle]):
      return right
   else:
      return middle

def _swap(data, pos1, pos2):
   temp = data[pos1]
   data[pos1] = data[pos2]
   data[pos2] = temp

if __name__ == "__main__":
   def sortTest():
      data = [3, 5, 2, 1, 72, -23, 89, 101, -11]
      sorted = quickSort(data)
      print(data)
      print(sorted)
      data.sort()
      assert sorted == data
   def medianOfThreeTest():
      assert _medianOfThree([3, 4, 5], 0, 2) == 1
   medianOfThreeTest()
   sortTest()
