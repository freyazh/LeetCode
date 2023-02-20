class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                # would be insert position
                res = mid + 1 
                left = mid + 1
            else:
                right = mid - 1

        return res 