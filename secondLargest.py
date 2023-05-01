# Given an array Arr of size N, print second largest distinct element from an array.

def print2largest(arr,n):
	if n<2:return -1
	l1,l2 = arr[0],-1
	for i in arr[1:]:
		if i>l1:
			l2,l1=l1,i
		elif i>l2 and i!=l1:
			l2=i
	return l2

arr = [12,35,10,2,34,1]
print(print2largest(arr,len(arr)))
