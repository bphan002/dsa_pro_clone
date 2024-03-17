class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # Remove pass and write code here
        planted_flowers = 0
       
        '''    
                            i 
            [[1, 0, 0, 1, 0, 0, 0, 1],2], False)
        '''
        return 1 if len(flowerbed) == 1 and flowerbed[0] == 0
        for i in range(len(flowerbed)):
            print('i',i)
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                # print('hit?', flowerbed[i], 'after', flowerbed[i+1])
                flowerbed[i] = 1
                planted_flowers +=1
            elif i == len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                planted_flowers +=1
            elif i > 0 and i != len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                planted_flowers +=1
        print('planted flowers', planted_flowers)
        return planted_flowers == n
    

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],1)) #should be true