class Solution:
    def search(self, nums, target):
        # Remove pass and write code here
        #  L     M     R
        # [4,5,6,7,0,1,2]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            
            #we know we are on the sorted side
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            #we know we are on the unsorted side 
            else: 
                #if the target is greater than the very far right
                #we know this was the biggest number possible so it has to be on the left
                # somewhere?
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        
        return - 1