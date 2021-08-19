class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            canFlowered = True
            if i != 0 and flowerbed[i - 1] == 1:
                canFlowered = False
            if flowerbed[i] == 1:
                canFlowered = False
            if i != len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                canFlowered = False

            if canFlowered:
                flowerbed[i] = 1
                n -= 1

        if n <= 0:
            return True

        return False