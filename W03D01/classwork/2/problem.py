class Solution:
    def searchMatrix(self, matrix, target):
        # Remove pass and write code here
    
        #first find the row the target can be in
        # target is 3
        '''
         [
          [1,3,5,7],  # top #right
          [10,11,16,20]
          [23,30,34,60] 
         ]
          
         target = 3
        '''
        # just trying to find which potential row the target is in
        top,bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            midpoint = top + ((bottom - top)//2)
            if target > matrix[midpoint][-1]:
                top = midpoint + 1
            elif target < matrix[midpoint][0]:
                bottom = midpoint - 1
            else:
                break       
        
        row = top + ((bottom - top)//2)
        inner_left = 0
        inner_right = len(matrix[row]) - 1
        
        while inner_left <= inner_right:
            midpoint = inner_left + ((inner_right - inner_left)//2)
            if matrix[row][midpoint] == target:
                return True
            elif target < matrix[row][midpoint]:
                inner_right = midpoint - 1
            elif target > matrix[row][midpoint]:
                inner_left = midpoint + 1
        
        return False






        
        
