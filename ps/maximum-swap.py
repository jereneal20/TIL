class Solution:

    def maximumSwap(self, num: int) -> int:
        arr_num = list(str(num))
        max_idx = min_idx = -1
        max_idx_use = min_idx_use = -1
        for idx in range(len(arr_num) - 1, -1, -1):
            if arr_num[idx] > arr_num[max_idx]:
                max_idx = idx

            if arr_num[idx] < arr_num[max_idx]:
                min_idx = idx
                max_idx_use = max_idx
                min_idx_use = min_idx

        arr_num[max_idx_use], arr_num[min_idx_use] = arr_num[min_idx_use], arr_num[max_idx_use]
        return int("".join(arr_num))