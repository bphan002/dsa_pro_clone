from collections import defaultdict

class Solution:
    def minSetSize(self, arr):
        num_count = defaultdict(int)
        for num in arr:
            num_count[num] += 1

        half = len(arr) // 2
        count = 0
        amt = 0
        sorted_dict_values = sorted(num_count.items(), key=lambda x: x[1], reverse=True)  
        print("Sorted:", sorted_dict_values)
        for num in sorted_dict_values:
            count += num[1]
            amt += 1
            if count >= half:
                return amt