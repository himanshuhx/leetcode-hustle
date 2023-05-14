# https://www.youtube.com/watch?v=w9JhOKb4tyk

class MyHashSet:

    def __init__(self):
        self.size = 10**6
        self.set = [None] * self.size
        
    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)
        
        if not self.set[hash_value]:
            self.set[hash_value] = [key]
        else:
            if not self.contains(key):
                self.set[hash_value].append(key)

    def remove(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)
        
        if self.set[hash_value]:
            if self.contains(key):
                self.set[hash_value].remove(key)

    def contains(self, key: int) -> bool:
        hash_value = self.calculate_hash_value(key)
        
        if self.set[hash_value]:
            for value in self.set[hash_value]:
                if value==key:
                    return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)