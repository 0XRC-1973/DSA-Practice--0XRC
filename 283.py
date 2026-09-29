# MOVES ZEROES
"""Link : https://leetcode.com/problems/move-zeroes/description/"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a += 1