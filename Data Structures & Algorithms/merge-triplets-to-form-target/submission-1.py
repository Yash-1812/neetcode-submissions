class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        max_a , max_b , max_c = target[0] , target[1] , target[2]
        current_a , current_b , current_c = 0 , 0 , 0

        for t in triplets:
            if t[0] > max_a or t[1] > max_b or t[2] > max_c:
                continue

            current_a = max(t[0] , current_a)
            current_b = max(t[1] , current_b)
            current_c = max(t[2] , current_c)

        return [current_a , current_b , current_c] == target