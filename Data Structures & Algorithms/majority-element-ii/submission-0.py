class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        treshold = (len(nums)) // 3
        for i in hashmap:
            if hashmap[i] > treshold:
                result.append(i)
        return result