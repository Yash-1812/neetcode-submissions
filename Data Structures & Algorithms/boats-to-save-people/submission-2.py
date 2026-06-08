class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        left , right = 0 , len(people) - 1
        people = sorted(people)
        while left <= right:
            if (people[left] + people[right]) == limit:
                boats += 1
                left += 1
                right -= 1
            elif (people[left] + people[right]) > limit:
                right -= 1
                boats += 1
            elif (people[left] + people[right]) < limit:
                boats += 1
                left += 1
                right -= 1
        
        return boats