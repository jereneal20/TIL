class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [(1 - cell for cell in row[::-1]) for row in image]

    def flipAndInvertImage2(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(int(len(image[i]) / 2)):
                tmp = image[i][j]
                image[i][j] = image[i][len(image[i]) - 1 - j]
                image[i][len(image[i]) - 1 - j] = tmp
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image


