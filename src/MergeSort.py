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
	while leftPos < len(left):
		data.append(left[leftPos])
		leftPos += 1
	while rightPos < len(right):
		data.append(right[rightPos])
		rightPos += 1
	return data

print(mergeSort([3, 5, 2, 1, 72, -23, 89, 101, -11]))
