g = [4,4,6]

def sumRecursion(arr):
  sum = 0
  if len(arr) == 0:
    return 0
  else:
    sum = sum + arr.pop(0) + sumRecursion(arr)
  return sum


print(sumRecursion(g))
