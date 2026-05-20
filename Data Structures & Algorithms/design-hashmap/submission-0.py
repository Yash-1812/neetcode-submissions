class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            c = 0
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    c = i
                    break
            self.values[c] = value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        c = 0
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                c = i
                break
        return self.values[c]

    def remove(self, key: int) -> None:
        if key in self.keys:
            c = 0
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    c = i
                    break
            self.keys.remove(key)
            del self.values[c]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)