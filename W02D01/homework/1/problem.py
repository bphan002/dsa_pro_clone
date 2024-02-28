class Solution:
    def numRescueBoats(self, people, limit):
        # Remove pass and write code here
        
        people.sort(reverse=True)
        left = 0
        right = len(people) - 1
        output = 0
        while left < right:
            if people[left] == limit:
                output +=1
                left +=1
            elif people[left] + people[right] == limit:
                left +=1
                right -=1

        return output
sol = Solution()
sol.numRescueBoats([3,2,2,1], 3)