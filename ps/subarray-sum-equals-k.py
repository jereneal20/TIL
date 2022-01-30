class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumArray = [0]
        sumMp = {0: 1}
        sum_so_far = 0
        count = 0
        for num in nums:
            sum_so_far += num
            sumArray.append(sum_so_far)
            if sum_so_far - k in sumMp:
                count += sumMp[sum_so_far - k]
            if sum_so_far not in sumMp:
                sumMp[sum_so_far] = 0
            sumMp[sum_so_far] += 1

        # print(sumArray)
        # print(sumMp)

        #         for i, _ in enumerate(sumArray):
        #             for _, num2 in enumerate(sumArray[i+1:]):
        #                 if num2 - sumArray[i] == k:
        #                     count += 1
        return count

        # [1,3,5,7,9] 12
        # [0,1,4,9,16,25]
        # 4 idx-2 idx
