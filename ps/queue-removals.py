from collections import *


def popXwithMaxNumIdx(deq, x, sol):
    max_idx = -1
    max_val = -1
    res = []
    iteration = 0
    while iteration < x and deq:
        val, idx = deq.popleft()
        res.append((val, idx))
        iteration += 1

    for idx, val in enumerate(res):
        if max_val < val[0]:
            max_idx = idx
            max_val = val[0]

    for idx, val in enumerate(res):
        if idx == max_idx:
            sol.append(val[1])
            continue
        deq.append((val[0] - 1 if val[0] > 0 else 0, val[1]))


def findPositions(arr, x):
    deq = deque()
    sol = []
    for idx, val in enumerate(arr):
        deq.append((val, idx + 1))
    iteration = x
    while iteration > 0:
        popXwithMaxNumIdx(deq, x, sol)

        iteration -= 1
    return sol


  # n_1 = 6
  # x_1 = 5
  # arr_1 = [1, 2, 2, 3, 4, 5]
  # expected_1 = [5, 6, 4, 1, 2]
  # output_1 = findPositions(arr_1, x_1)
  # check(expected_1, output_1)
  #
  # n_2 = 13
  # x_2 = 4
  # arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  # expected_2 = [2, 5, 10, 13]