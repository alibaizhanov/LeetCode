n = [3,4,1,2,9,7,12,10,22,23,23,12,11]


def BubbleSort (arr):
  length = len(arr)

  n = 0
  while length > n:
    n = n + 1
    for i in range(length - n):
      if arr[i] > arr[i+1]:
         temp = arr[i]
         arr[i] = arr[i+1]
         arr[i+1] = temp

  return arr

print(BubbleSort(n))
