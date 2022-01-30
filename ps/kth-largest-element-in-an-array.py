class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            i = l
            while i < r:
                if nums[i] < nums[r]:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                i += 1
            nums[r], nums[l] = nums[l], nums[r]
            return l

        random.shuffle(nums)
        l, r = 0, len(nums) - 1
        while True:
            pivot = partition(l, r)
            # print(nums)
            # print(str(l) + " " + str(r) + " " + str(pivot))
            if pivot == len(nums) - k:
                return nums[pivot]
            elif pivot < len(nums) - k:
                l = pivot + 1
            else:
                r = pivot - 1

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        mp = defaultdict(lambda: 0)
        for num in nums:
            mp[num] += 1

        count = 0
        for num in range(10000, -10001, -1):
            count += mp[num]
            if count >= k:
                return num

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)

        val = None
        for i in range(k):
            val = heapq._heappop_max(nums)
        return val
