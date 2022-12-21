from typing import List
from collections import deque, defaultdict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 1:
            return True

        queue = deque()
        queue.appendleft(0)

        visited = set()
        while queue:
            room = queue.pop()
            visited.add(room)

            for neighbor in rooms[room]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return len(visited) == len(rooms)