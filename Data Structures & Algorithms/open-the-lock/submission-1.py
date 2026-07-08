class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if '0000' in visited:
            return -1
        
        queue = deque([('0000' , 0)])
        visited.add('0000')
        while queue:
            curr , moves = queue.popleft()
            if curr == target:
                return moves

            for i in range(4):
                digit = int(curr[i])
                for turn in (-1 , 1):
                    next_digit = (digit + turn) % 10
                    next_state = curr[:i] + str(next_digit) + curr[i+1:]

                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state , moves + 1))
        return -1