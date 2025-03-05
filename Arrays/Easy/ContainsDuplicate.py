from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i,num in enumerate(nums): # index and iterate through list
            if num in hashMap:  # if we have seen this number, return True
                return True
            else:
                hashMap[num] = i # otherwise add the number to the hashmap/dictionary

        return False # false if we never find a duplicate