# First version implementation
def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  return None

def verify(index):
  if index is not None:
    print("Target value found at index ", index)
  else:
    print("Value not found in the list")

numbers = [2,4,3,6,8,9,7,1,5,10]
numbers.sort()
# numbers = [1,2,3,4,5,6,7,8,9,10]

results = binary_search(numbers, 1)

verify(results)