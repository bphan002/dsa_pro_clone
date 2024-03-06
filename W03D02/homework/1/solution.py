class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1: 
                continue
            
            left_valid = (i == 0) or (flowerbed[i-1] == 0)
            right_valid = (i == len(flowerbed)-1 )or (flowerbed[i+1] == 0 )

            if left_valid and right_valid:
                flowerbed[i] = 1
                count += 1

        return count >= n