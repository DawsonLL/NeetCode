from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for i in range(len(strs)):
            key = tuple(sorted(strs[i])) # we convert the result of sorted into a tuple, because it turns the str in a list of characters
            dict.setdefault(key, []).append(strs[i]) # setdefault creates a sublist if the key does not exist, otherwise it will return the existing list for the given key

        return dict.values() # return all the sublists in the dictionary