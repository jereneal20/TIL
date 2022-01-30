class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not len(arr) >= 3:
            return False
        if not (arr[0] < arr[1]):
            return False
        increasing = True
        i = 1
        while i < len(arr):
            if arr[i - 1] == arr[i]:
                return False
            if not increasing and arr[i - 1] < arr[i]:
                return False
            if increasing and arr[i - 1] < arr[i]:
                pass
            elif increasing and arr[i - 1] > arr[i]:
                increasing = False
            elif not increasing and arr[i - 1] > arr[i]:
                pass

            i += 1
        if increasing:
            return False
        return True