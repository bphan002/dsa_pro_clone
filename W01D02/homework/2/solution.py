from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes):
        ans = []
        
        sz_to_group = defaultdict(list)
        
        for person, group in enumerate(groupSizes):
            sz_to_group[group].append(person)
            
            if len(sz_to_group[group]) == group:
                ans.append(sz_to_group.pop(group))
                
        return ans
