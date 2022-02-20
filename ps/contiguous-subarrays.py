import math

def count_subarrays(arr):
    res = []
    maximum_left = []
    maximum_right = []
    mx_left = []
    mx_right = []
    for idx, val in enumerate(arr):
        while len(maximum_left) != 0 and arr[maximum_left[-1]] < arr[idx]:
            maximum_left.pop()
        if len(maximum_left) == 0:
            mx_left.append(-1)
        else:
            mx_left.append(maximum_left[-1])
        maximum_left.append(idx)

    idx = len(arr) - 1
    while idx >= 0:
        while len(maximum_right) != 0 and arr[maximum_right[-1]] < arr[idx]:
            maximum_right.pop()
        if len(maximum_right) == 0:
            mx_right.append(len(arr))
        else:
            mx_right.append(maximum_right[-1])
        maximum_right.append(idx)
        idx -= 1

    mx_right = mx_right[::-1]

    for idx, val in enumerate(arr):
        res.append(idx - mx_left[idx] + mx_right[idx] - idx - 1)
    return res


# test_1 = [3, 4, 1, 6, 2]
# expected_1 = [1, 3, 1, 5, 1]
# output_1 = count_subarrays(test_1)
# check(expected_1, output_1)
#
# test_2 = [2, 4, 7, 1, 5, 3]
# expected_2 = [1, 2, 6, 1, 3, 1]
# output_2 = count_subarrays(test_2)
# check(expected_2, output_2)