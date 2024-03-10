import math

class Solution:
    def minEatingSpeed(self, piles, h):
        # Remove pass and write code here
        left = 1
        right = max(piles)
        mins = float('inf')

        while left <= right:
            mid = left + (right - left)//2
            time = 0

            for pile in piles:
                time += math.ceil(pile/mid)
                print(math.ceil(pile/mid))
         
            if time <= h:
                mins = min(mins, mid)
                right = mid - 1
            else:
                left = mid + 1

        return mins