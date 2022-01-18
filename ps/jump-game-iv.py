class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mp = {}
        visited = set()
        for idx, value in enumerate(arr):
            if value not in mp:
                mp[value] = []
            mp[value].append(idx)

        deq = deque()
        deq.append([0, 0])

        while True:
            steps, index = deq.popleft()
            if index == len(arr) - 1: return steps

            for neigh in [index - 1, index + 1]:
                if 0 <= neigh < len(arr) and arr[neigh] in mp:
                    if neigh not in visited:
                        deq.append([steps + 1, neigh])
                        visited.add(neigh)

            if arr[index] in mp:
                for idx in mp[arr[index]]:
                    if idx not in visited:
                        deq.append([steps + 1, idx])
                        visited.add(idx)
                del mp[arr[index]]

    def minJumps2(self, arr: List[int]) -> int:
        # dp로 왼쪽에서 오른쪽으로 업데이트하고, 업데이트되면 왼쪽을 보는걸 하려고했으나, 1 2 3 4 5 6 7 8 9 3 10 11 12 13 5 와 같이 앞뒤로 왔다갔다 해서 결론에 다다르는걸 커버하지 못한다.
        mp = {}
        dp = [0] * len(arr)  # for i in range(len(arr))]
        mp[arr[0]] = 0

        for i in range(1, len(arr)):
            if arr[i] in mp and mp[arr[i]] < dp[i - 1]:
                dp[i] = mp[arr[i]] + 1

                j = i - 1
                while dp[j] > dp[j + 1] + 1:
                    dp[j] = dp[j + 1] + 1
                    if arr[j] not in mp or mp[arr[j]] > dp[j]:
                        mp[arr[j]] = dp[j]
                    j -= 1
            else:
                dp[i] = dp[i - 1] + 1

            if arr[i] not in mp or mp[arr[i]] > dp[i]:
                mp[arr[i]] = dp[i]

        return dp[len(arr) - 1]

    #     10 12 13
    # 10  0
    # 12     1
    # 13

    # [100,-23,-23,404,100,23,23,23,3,404]
    #    0  1   2   3   1   2  3  3 4  3
    #               2

    # [7872,-2477,-4437,7504,7828,3248,-8793,-7246,2741,4359,-6373,3408,-2938,-3233,-8880,-6081,295,8614,-24,-897,7990,9365,9056,-8547,-494,-2455,-9761,7659,3639,-4437,-7767,-897,7896,9466,-8697,2666,-8042,3377,6422,-8219,-1206,-7561,-2683,-6029,2172,-1120,730,9423,2495,-8880,1174]