# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed_len = len(flowerbed)

        for i in range(flowerbed_len):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == flowerbed_len - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1

        return True if n <= 0 else False

data = Solution()
print(data.canPlaceFlowers([1,0,0,0,0,0,0,0,1], 3))