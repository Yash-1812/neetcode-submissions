class MyHashSet:

    def __init__(self):
        self.hashmap = []

    def add(self, key: int) -> None:
        if key not in self.hashmap:
            self.hashmap.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashmap else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)