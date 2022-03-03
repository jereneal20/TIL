import math
from collections import *

def getMilestoneDays(revenues, milestones):
    mp = defaultdict(list)
    sorted_milestones = []
    for idx, milestone in enumerate(milestones):
        sorted_milestones.append((milestone, idx))
    sorted_milestones.sort()

    total = 0
    res = [-1] * len(milestones)
    for idx, milestone in enumerate(milestones):
        mp[milestone] = idx

    i = 0
    for idx, revenue in enumerate(revenues):
        total += revenue
        while sorted_milestones[i][0] <= total:
            res[sorted_milestones[i][1]] = idx + 1
            i += 1
            if i == len(sorted_milestones):
                return res

    return res

  # revenues_1 = [100, 200, 300, 400, 500]
  # milestones_1 = [300, 800, 1000, 1400]
  # expected_1 = [2, 4, 4, 5]
  #
  # revenues_2 = [700, 800, 600, 400, 600, 700]
  # milestones_2 = [3100, 2200, 800, 2100, 1000]
  # expected_2 = [5, 4, 2, 3, 2]
