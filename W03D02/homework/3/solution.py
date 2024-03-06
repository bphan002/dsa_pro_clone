from collections import defaultdict

class Solution:
    def minSetSize(self, arr):
        
        frequencies = defaultdict(int)
        
        for n in arr:
            frequencies[n] += 1
        
        # sort elements by frequency
        frequencies = [freq for freq in frequencies.values()]
        frequencies.sort(reverse=True)
        
        total_removed = 0
        set_size = 0
        
        for freq in frequencies:
            total_removed += freq
            set_size += 1
            if total_removed >= len(arr)//2:
                break
                
        return set_size