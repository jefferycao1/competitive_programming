# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
# Only O(1) extra space
# input is list of numbers
# output is it ordered the problem wants it to be 

array = [1, 2, 3, -4, -1, 4]

def rotate(array, start, end):
	temp = array[end]
	for i in range(end, start, -1):
		array[i] = array[i - 1]
	array[start] = temp

	return array

def solve(array):
	negative = True
	for i in range(len(array)):
		print(i, end = " ")
		print(array)
		if(negative):
			for j in range(i, len(array)):
				if(array[j] >= 0):
					continue
				else:
					#print(array, i, j)
					array = rotate(array, i, j)
					negative = False
					break
		else:
			for k in range(i, len(array)):
				if(array[k] < 0):
					continue
				else:
					array = rotate(array, i, k)
					negative = True
					break
	return array

array = solve(array)
print(array)


