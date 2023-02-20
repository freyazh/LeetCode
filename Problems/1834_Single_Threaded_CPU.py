from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasksHeap = []

        for i, (et, pt) in enumerate(tasks):
            # heapq: sort by the first element of the tuple
            heapq.heappush(tasksHeap, (et, pt, i))

        availableTask = []
        res = []

        while tasksHeap or availableTask:
            if availableTask:
                pt, idx = heapq.heappop(availableTask)
            else:
                # smallest enque time first out
                et, pt, idx = heapq.heappop(tasksHeap)
                finishTime = et

            finishTime += pt
            res += [idx]

            while tasksHeap and tasksHeap[0][0] <= finishTime:
                et, pt, idx = heapq.heappop(tasksHeap)
                # sort avaliable tasks by processing time
                heapq.heappush(availableTask, (pt, idx))

        return res


# Test Cases:
# tasks = [[1,2],[2,4],[3,2],[4,1]]
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
s = Solution()
print(s.getOrder(tasks))
