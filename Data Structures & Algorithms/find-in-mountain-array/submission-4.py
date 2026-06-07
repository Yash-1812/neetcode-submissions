class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l , r = 1 , n - 2
        m = 0
        while l <= r:
            m = (l + r) // 2
            left , mid , right = mountainArr.get(m - 1) , mountainArr.get(m) , mountainArr.get(m + 1)
            if left < mid < right:
                l = mid + 1
            elif left > mid > right:
                r = mid - 1
            else:
                break
        peak = m
        l , r = 0 , peak
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid
        l  , r = peak , n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val > target:
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                return mid
        return -1