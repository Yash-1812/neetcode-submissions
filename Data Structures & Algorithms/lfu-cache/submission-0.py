class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.count = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        self.count.move_to_end(key)
        self.count[key] += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.count[key] += 1
            self.cache.move_to_end(key)
            self.count.move_to_end(key)
        elif len(self.cache) == self.capacity:
            min_freq = min(self.count.values())
            min_keys = [k for k , v in self.count.items() if v == min_freq]
            if len(min_keys) == 1:
                del self.count[min_keys[0]]
                del self.cache[min_keys[0]]
            else:
                last_key = min_keys[0]
                del self.cache[last_key]
                del self.count[last_key]
            self.cache[key] = value
            self.count[key] = 1
            self.cache.move_to_end(key)
            self.count.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
            self.count[key] = 1
            self.count.move_to_end(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)