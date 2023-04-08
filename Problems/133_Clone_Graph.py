# https://leetcode.com/problems/clone-graph/solutions/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import copy 
class Solution:
    visited = []
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node'):
            if not node:
                return None
            if node.neighbors == []:
                return copy.deepcopy(node)

            if node not in self.visited:
                ans = copy.deepcopy(node)
                self.visited.append(node)
                for n in node.neighbors:
                    if n not in self.visited:
                        dfs(n)
                return ans
            else:
                return None

        return dfs(node)

