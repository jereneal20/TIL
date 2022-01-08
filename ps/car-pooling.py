class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = {}
        for trip in trips:
            if trip[1] not in dic:
                dic[trip[1]] = 0
            dic[trip[1]] += trip[0]
            if trip[2] not in dic:
                dic[trip[2]] = 0
            dic[trip[2]] -= trip[0]

        cur_capacity = 0
        for i in range(1002):
            if cur_capacity > capacity:
                return False
            if i in dic:
                cur_capacity += dic[i]

        return True


