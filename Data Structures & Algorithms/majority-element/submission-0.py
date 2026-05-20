class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n , 0)

        return max(hashmap , key = hashmap.get)