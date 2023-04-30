# At least two greater elements
# Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.

def findElements(arr,n):
	arr.sort()
	return arr[:-2]

arr = [2,8,7,1,5]
print(findElements(arr,len(arr)))
