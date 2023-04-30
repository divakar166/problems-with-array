# Value equal to index
# Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
# Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. 
# Follows 1-based indexing of the array.

def valueEqualToIndex(arr,n):
	ans = []
	for i in range(n):
		if arr[i] ==i+1:
			ans.append(arr[i])
	return ans

arr = [15,2,45,9,5]
print(valueEqualToIndex(arr,len(arr)))
