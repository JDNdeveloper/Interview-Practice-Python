# Author: Jayden Navarro
# Date: 10/14/2015

def mergeSort(data):
   length = len(data)
   if length <= 1:
      return data
   half = int(length / 2)
   left = mergeSort(data[:half])
   right = mergeSort(data[half:])
   return merge(left, right)

def merge(left, right):
   leftPos = 0
   rightPos = 0
   data = []
   while leftPos < len(left) and rightPos < len(right):
      if left[leftPos] < right[rightPos]:
         data.append(left[leftPos])
         leftPos += 1
      else:
         data.append(right[rightPos])
         rightPos += 1
   data.extend(left[leftPos:])
   data.extend(right[rightPos:])
   return data

if __name__ == "__main__":
   data = [3, 5, 2, 1, 72, -23, 89, 101, -11]
   sorted = mergeSort(data)
   print(data)
   print(sorted)
   data.sort()
   assert sorted == data
