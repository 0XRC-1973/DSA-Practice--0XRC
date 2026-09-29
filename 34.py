# FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY
"""Link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(is_first: bool) -> int:
            low, high = 0, len(nums) - 1
            bound = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return bound

        start = findBound(is_first=True)
        if start == -1:
            return [-1, -1]

        end = findBound(is_first=False)
        return [start, end]