# Stack implementation using Array

arr = []

def push(data):
	return arr.append(data)

def pop():
	if len(arr)==0:
		return -1
	else:
		return arr.pop()

push(4)
push(3)
pop()

print(arr)
