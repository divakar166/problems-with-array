# Implementation of a Queue using an Array

arr = []

def push(x):
	return arr.append(x)

def pop():
	if len(arr) == 0:
		return -1
	else:
		return arr.pop(0)

push(4)
push(5)
pop()
push(1)
print(arr)
