class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr) == 1:
            return arr
        output = []
        spare = []
        for i , n in enumerate(arr):
            spare.append((abs(x-n),i))
        spare = sorted(spare)
        for _ in range(k):
            i , j = spare.pop(0)
            output.append(arr[j])
        return sorted(output)
