g = [4,45,6,9,1,3,7,8,21,19,20,21,86,5]


###Time complexity O(n**2)
def SelectSorted(arr):

  smallest = arr[0]
  smallectIndex = 0

  for i in range(1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallectIndex = i

  return smallectIndex


def selectionSort(arr):
  newArr = []

  for i in range(len(arr)):
    smallest = SelectSorted(arr)
    newArr.append(arr.pop(smallest))

  return newArr


print(selectionSort(g))
