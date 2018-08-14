g = [4,45,6,9,1,3,7,8,21,19,20,21,86,5]
print(g[1::])

def quickSort(arr):

  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    left_side = [i for i in arr[1::] if i <= pivot]
    right_side = [j for j in arr[1::] if j > pivot]

    return quickSort(left_side) + [pivot] + quickSort(right_side)


print(quickSort(g))
