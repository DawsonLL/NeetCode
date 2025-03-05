from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairmap = {}
        for i,num in enumerate(nums):
            complement = target-num # find the other addend
            if complement in pairmap:
                return [pairmap[complement], i]
            pairmap[num] = i # add
        return [] # if no complement in found, return