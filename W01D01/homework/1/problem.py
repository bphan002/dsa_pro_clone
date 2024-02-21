class Solution:
    def groupAnagrams(self, strs):
        # Remove pass and write code here
        hashmap = {}
        res = []
        for word in strs:
            key = self.abc_order(word)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        # for key in hashmap:
        #     values = hashmap[key]
        #     res.append(values)
        #or res.extend(hashmap.values())
        # or.... return list(hashmap.values())       
        #.values create a view object
        return list(hashmap.values())
    def abc_order(self,word):
        word_list = list(word)
        word_list.sort()
        new_word ="".join(word_list)
        return new_word

sample = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sample.groupAnagrams(strs))