class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n < 2:
            return [i for i in range(n)]
        adj_list = collections.defaultdict(set)
        degree = [0] * n
        for u , v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
            degree[u] += 1
            degree[v] += 1
        leaves = deque([i for i in range(n) if degree[i] == 1])
        remaining = n
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for nei in adj_list[leaf]:
                    adj_list[nei].remove(leaf)
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
        return list(leaves)