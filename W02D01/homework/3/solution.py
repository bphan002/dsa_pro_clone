class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        left = 0
        subarr_count = 0
        total = 0
        n_count = 0
        
        
        for right in range(len(arr)):
            total += arr[right]
            n_count += 1
            
            while right-left+1 == k:
                if total/n_count >= threshold:
                    subarr_count += 1
                    
                total -= arr[left]
                n_count -= 1
                left += 1
                
        return subarr_count