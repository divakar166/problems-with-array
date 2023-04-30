# Palindromic Array
# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

def PalinArray(arr,n):
  for i in range(0,n):
    r = str(arr[i])[::-1]
    if arr[i] != int(r):
      return False
    
  return True

arr = [111,121,222,333]
print(PalinArray(arr,len(arr)))
