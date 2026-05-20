from collections import defaultdict , deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(set)

        for a , b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_nodes = len(leaves)
            remaining_nodes -= leaf_nodes

            for _ in range(leaf_nodes):
                node = leaves.popleft()
                neighbour = graph[node].pop()
                graph[neighbour].remove(node)
                if len(graph[neighbour]) == 1:
                    leaves.append(neighbour)
        
        output = [i for i in leaves]
        return output
        