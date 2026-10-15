class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [i for i in range(n)]
        adj_list = collections.defaultdict(set)
        indegree = [0] * n
        for u , v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
            indegree[u] += 1
            indegree[v] += 1
        leaves = deque([i for i in range(n) if indegree[i] == 1])
        remaining = n
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for nei in adj_list[leaf]:
                    indegree[nei] -= 1
                    adj_list[nei].remove(leaf)
                    if indegree[nei] == 1:
                        leaves.append(nei)
        return list(leaves)