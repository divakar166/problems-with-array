# Given a stream of incoming numbers, find average or mean of the stream at every point.

def streamAvg(arr,n):
	avg = []
	for i in range(n):
		avg.append(sum(arr[:i+1])/(i+1))
	return avg

arr = [10,20,30,40,50]
print(streamAvg(arr,len(arr)))
