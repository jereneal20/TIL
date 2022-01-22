class DLinkedList:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def append(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def appendLeft(self, node):
        node.next = self
        node.prev = self.prev
        self.prev.next = node
        self.prev = node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_cap = 0
        self.mp = {}
        self.head = DLinkedList(-1, -1)
        self.last = DLinkedList(-1, -1)
        self.head.next = self.last
        self.last.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        value, node = self.mp[key]
        node.delete()
        self.last.appendLeft(node)
        return value

    def put(self, key: int, value: int) -> None:
        node = DLinkedList(key, value)
        if key in self.mp:
            self.mp[key][1].delete()
            self.mp[key] = (value, node)
            self.last.appendLeft(node)
            return

        if self.current_cap == self.capacity:
            print(self.head.next.key)
            del self.mp[self.head.next.key]
            self.head.next.delete()
            self.current_cap -= 1

        self.mp[key] = (value, node)
        self.last.appendLeft(node)

        self.current_cap += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)