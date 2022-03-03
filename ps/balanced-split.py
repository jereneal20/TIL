
def balancedSplitExists(arr):
  arr.sort()
  i, j = 0, len(arr) - 1
  l, r = sum(arr), 0
  if sum(arr) == 0:
    return True

  while 0 <= j:
    l -= arr[j]
    r += arr[j]
    if l < r:
      return False
    if l == r and arr[j-1] < arr[j]:
      return True
    j -= 1

  return False


  # arr_1 = [2, 1, 2, 5]
  # expected_1 = True
  #
  # arr_2 = [3, 6, 3, 4, 4]
  # expected_2 = False