# https://leetcode.com/problems/minimum-time-to-complete-trips/

from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(givenTime):
            trips = 0
            for t in time:
                trips += givenTime // t
            if trips >= totalTrips:
                return True
            return False
    
        left = 1
        right = max(time) * totalTrips
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

