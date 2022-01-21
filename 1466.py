"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

"""
from typing import List

# t = O(n)
# s = O(n)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = { (a,b) for a, b in connections }
        neighbours = { city:[] for city in range(n) }
        visited = set()
        changes = 0

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal edges, neighbours, visited, changes

            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue

                if (neighbour, city) not in edges:
                    changes += 1
                visited.add(neighbour)

                dfs(neighbour)
        
        visited.add(0)
        dfs(0)

        return changes

solution = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

print(solution.minReorder(n, connections))
