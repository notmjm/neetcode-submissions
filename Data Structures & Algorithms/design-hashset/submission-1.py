class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        for i in self.data:
            if [key] == i:
                return
            
        self.data.append([key])

    def remove(self, key: int) -> None:
        for i in self.data:
            if [key] == i:
                self.data.remove([key])
                


    def contains(self, key: int) -> bool:
        for i in self.data:
            if [key] == i:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)