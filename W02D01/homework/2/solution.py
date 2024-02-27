from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left, right = 0,0
        longest = 0
        count = defaultdict(int)
        
        for right in range(len(s)):
            count[s[right]] += 1

            while len(count) > 2:
                char = s[left]
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
                left += 1
            
            longest = max(longest, right-left+1)
        
        return longest