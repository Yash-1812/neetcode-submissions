class TimeMap:

    def __init__(self):
        self.my_dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp , value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        res = ''
        left = 0
        right = len(self.my_dict[key]) - 1
        arr = self.my_dict[key]
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res