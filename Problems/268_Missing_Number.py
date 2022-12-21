class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exitsNum = set()

        for i in range(0, len(nums)):
            exitsNum.add(nums[i])

        for i in range(0, len(nums)+1):
            if not i in exitsNum:
                return i

        return -1