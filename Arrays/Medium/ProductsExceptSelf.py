from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        total = 1
        hold = 1

        for i in range(len(nums)):
            hold *= nums[i]
            # This condition ensures that if we encounter only one zero, we store the total for that index later on.
            # It will also correctly handle the case for when there is more than two zeroes, in which case the whole list would equal 0.
            if nums[i] == 0:
                hold = total
            total *= nums[i]
            
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(total//nums[i])
            else:
                arr.append(hold)

        return arr