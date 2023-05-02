# Play with an Array
# Given an unsorted array arr of size N, rearrange the elements of array such that number at the odd index is greater than the number at the previous even index. 
# The task is to complete the function formatArray() which will return formatted array.

def formatArray(arr,n):
	for i in range(1,n,2):
		if arr[i-1]>arr[i]:
			arr[i-1],arr[i]=arr[i],arr[i-1]
	return arr

arr = [5,4,3,2,1]
print(formatArray(arr,len(arr)))

# Output is [4,5,2,3,1]
