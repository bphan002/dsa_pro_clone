class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        # Remove pass and write code here
        #Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size k and average greater than or equal to threshold.

## **Example 1:**
              #l
#Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
                  #r
#Output: 3
#Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
        
        res = 0
        total = 0
        right = 0
        left = 0
        while right < k:
            total += arr[right]
            right+=1

        if total/k > threshold:
            res += 1
        for i in range(k,len(arr)):
            total -= arr[left]
            left+=1
            total += arr[i]
            print('average',total/k)
            if total/k >= threshold:
                print('hi')
                res += 1


        print(res)
        return res


sol = Solution()

sol.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)