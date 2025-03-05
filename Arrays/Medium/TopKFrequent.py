from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        
        # create a frequency dict
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1

        # iterate through the dict, create a list of [value,key] pairs, sorted in ascending order
        arr = []
        for num,cnt in dict.items():
            arr.append([cnt,num])
        arr.sort()
        
        # create a list containing k of the most frequent integers, by popping off the end of the arr list and saving the popped key value into result
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result