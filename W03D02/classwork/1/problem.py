class Solution:
    def maxNumberOfApples(self, weight):
        basket_weight = 0
        apples = 0
        sorted(weight)
        
        for appleWeight in weight:
            if basket_weight + appleWeight <= 5000:
                apples +=1
                basket_weight += appleWeight
            else:
                break
        
        return apples