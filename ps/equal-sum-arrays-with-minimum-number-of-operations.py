class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums2) < sum(nums1):
            return self.minOperations(nums2, nums1)
        nums1.sort()
        nums2.sort()
        num1_sum = sum(nums1)
        num2_sum = sum(nums2)

        count = 0
        num1_idx = 0
        num2_idx = len(nums2) - 1
        # num1 [1,1,2,2,2,2]
        # num2 [1,2,3,4,5,6]
        while num1_sum < num2_sum:
            if num1_idx == len(nums1) and num2_idx == -1:
                break

            elif num2_idx == -1 or (num1_idx != len(nums1) and nums1[num1_idx] < (7 - nums2[num2_idx])):
                num1_sum += (6 - nums1[num1_idx])
                num1_idx += 1
            else:
                num2_sum -= nums2[num2_idx] - 1
                num2_idx -= 1
            count += 1

        if num1_sum < num2_sum:
            return -1

        return count