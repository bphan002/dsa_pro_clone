class Solution:
    def maxNumberOfApples(self, weight):
        weight.sort()
        apples = 0
        total_weight = 0
        
        for w in weight:
            total_weight += w
            if total_weight > 5000:
                break
            
            apples += 1
            
        return apples