class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_ele = 0
            for j in range(i + 1 , len(arr)):
                max_ele = max(max_ele , arr[j])
            arr[i] = max_ele
        arr[len(arr) - 1] = -1
        return arr