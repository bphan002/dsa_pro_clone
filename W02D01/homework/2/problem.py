from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Remove pass and write code here
        left = 0
        right = 0
        longest = 0
        #                  l
        #    Input: s = "eceba"
        #                   r
         ##   Output: 3
           # Explanation: The substring is "ece" which its length is 3.
        char_count = defaultdict(int)
        # print(char_count)
        while right < len(s):
            char_count[s[right]] +=1

            while left < len(s) and len(char_count.keys()) > 2:
                # print(char_count)
                # print('right',right, 'left', left)
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            longest = max(longest, right-left + 1)
            right += 1
            print(char_count)
        print('longest',longest)
        return longest

lengths = Solution()            
lengths.lengthOfLongestSubstringTwoDistinct("ccaabbb")